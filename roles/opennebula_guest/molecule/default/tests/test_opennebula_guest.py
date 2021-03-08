import pytest


@pytest.mark.parametrize('name', [
    'one-context', 'cloud-utils-growpart', 'parted', 'open-vm-tools',
    'qemu-guest-agent'
])
def test_package_installed(host, name):
    pkg = host.package(name)
    assert pkg.is_installed


def test_one_context_service(host):
    service = host.service('one-context')
    assert service.is_enabled
