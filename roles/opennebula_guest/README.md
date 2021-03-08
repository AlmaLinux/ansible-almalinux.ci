# almalinux.ci.opennebula_guest

An Ansible role that installs OpenNebula contextualization tools on a virtual
machine.


## Role Variables

Role variables and their default values are listed below:

* `one_context_version: '5.12.0.2'` - one-context package version.
* `one_context_release: '1'` - one-context package release.
* `one_context_url: "https://github.com/OpenNebula/addon-context-linux/releases/download/v{{ one_context_version }}/one-context-{{ one_context_version }}-{{ one_context_release }}.el{{ ansible_distribution_major_version }}.noarch.rpm"` - one-context package download URL.


## License

MIT


## Authors

* [Eugene Zamriy](https://github.com/ezamriy)
