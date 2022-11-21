# -*- mode:python; coding:utf-8; -*-

"""
almalinux.ci.nvidia_cuda_samples Ansible role tests.
"""

import os

import pytest


@pytest.mark.parametrize('sample',
                         ['0_Introduction', '1_Utilities',
                          '2_Concepts_and_Techniques', '3_CUDA_Features',
                          '4_CUDA_Libraries', '5_Domain_Specific',
                          '6_Performance'])
def test_sample_installed(host, sample):
    sample_dir_path = os.path.join('/usr/local/cuda/samples/', sample)
    sample_dir = host.file(sample_dir_path)
    assert sample_dir.is_directory
    readme_file = host.file(os.path.join(sample_dir_path, 'README.md'))
    assert readme_file.is_file
