import pytest


@pytest.mark.parametrize('name', [
    'mlnx-ofa_kernel', 'mlnx-ofa_kernel-modules', 'rdma-core', 'knem',
    'knem-modules', 'mlnx-tools', 'mlnx-fw-updater', 'libibverbs-utils',
    'librdmacm', 'mlnx-iproute2'
])
def test_package_installed(host, name):
    pkg = host.package(name)
    assert pkg.is_installed


def test_openibd_service(host):
    service = host.service('openibd')
    assert service.is_enabled


def test_tmp_dir_removed(host):
    with host.sudo():
        for f_name in host.file('/root').listdir():
            assert f_name.startswith('mlnx_ofed') is not True


def test_perftest_versionlock(host):
    with host.sudo():
        cmd = host.run('dnf versionlock list')
        assert 'perftest' in cmd.stdout

def test_openmpi_versionlock(host):
    if int(host.system_info.release[0]) != 9:
        pytest.skip('required only on EL9')
    with host.sudo():
        cmd = host.run('dnf versionlock list')
        assert 'openmpi' in cmd.stdout
