# almalinux.ci.upgrade_and_reboot

An Ansible role that upgrades all packages to their latest versions and
reboots a host.


## Role Variables

Role variables and their default values are listed below:

* `reboot_connect_timeout: 5` - number of seconds to sleep before retrying check.
* `reboot_timeout: 600` - maximum number of seconds to wait for a host return.
* `reboot_post_reboot_delay: 15` - number of seconds to wait before starting checking.


## License

MIT


## Authors

* [Eugene Zamriy](https://github.com/ezamriy)
