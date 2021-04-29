def test_firstboot_disabled(host):
    cfg_file = host.file('/etc/sysconfig/firstboot')
    assert cfg_file.exists
    assert cfg_file.user == 'root'
    assert cfg_file.group == 'root'
    assert cfg_file.mode == 0o644
    assert cfg_file.contains(r'^RUN_FIRSTBOOT=NO$')
