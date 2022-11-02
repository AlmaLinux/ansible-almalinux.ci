# -*- mode:python; coding:utf-8; -*-

"""
almalinux.ci.nvidia_cuda_repo Ansible role tests.
"""

import configparser

import pytest


@pytest.fixture(scope='module')
def distro_ver(host):
    return host.system_info.release[0]


@pytest.fixture(scope='module')
def repo_file_path(distro_ver):
    return f'/etc/yum.repos.d/cuda-rhel{distro_ver}.repo'


@pytest.fixture(scope='module')
def repo_arch(host):
    arch = host.system_info.arch
    if arch == 'aarch64':
        return 'sbsa'
    elif arch in ('x86_64', 'ppc64le'):
        return arch
    else:
        raise ValueError(f'unsupported architecture {arch}')


def test_cuda_repo_file(host, repo_file_path):
    repo_file = host.file(repo_file_path)
    assert repo_file.exists
    assert repo_file.user == 'root'
    assert repo_file.group == 'root'
    assert repo_file.mode == 0o644


def test_cuda_repo_config(host, repo_file_path, repo_arch, distro_ver):
    content = host.file(repo_file_path).content_string
    config = configparser.ConfigParser()
    config.read_string(content)
    repo_name = f'cuda-rhel{distro_ver}-{repo_arch}'
    assert config.has_section(repo_name)
    section = config[repo_name]
    assert section['name'] == repo_name
    assert section['enabled'] == '1'
    assert section['gpgcheck'] == '1'
    repo_url = (f'https://developer.download.nvidia.com/compute/cuda/repos/'
                f'rhel{distro_ver}/{repo_arch}')
    key_url = f'{repo_url}/D42D0685.pub'
    assert section['gpgkey'] == key_url
    assert section['baseurl'] == repo_url
