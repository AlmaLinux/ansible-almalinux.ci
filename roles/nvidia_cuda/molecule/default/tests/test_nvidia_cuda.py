# -*- mode:python; coding:utf-8; -*-

"""
almalinux.ci.nvidia_cuda Ansible role tests.
"""


def test_cuda_toolkit_profile(host):
    profile_path = '/etc/profile.d/cuda-toolkit.sh'
    profile = host.file(profile_path)
    assert profile.exists
    assert profile.user == 'root'
    assert profile.group == 'root'
    assert profile.mode == 0o644
    context = host.run(f'ls -Z {profile_path} | cut -d " " -f 1').stdout.strip()
    assert context == 'system_u:object_r:bin_t:s0'


def test_cuda_path(host):
    path = host.environment()['PATH'].split(':')
    assert '/usr/local/cuda/bin' in path


def test_cuda_ld_library_path(host):
    ld_path = host.environment()['LD_LIBRARY_PATH'].split(':')
    assert '/usr/local/cuda/lib64' in ld_path


def test_cuda_toolkit_installed(host):
    distro_ver = host.system_info.release[0]
    if distro_ver == '8':
        toolkit_ver = '11-6'
    elif distro_ver == '9':
        toolkit_ver = '11-7'
    else:
        raise ValueError(f'unsupported EL version {distro_ver}')
    assert host.package(f'cuda-toolkit-{toolkit_ver}').is_installed
