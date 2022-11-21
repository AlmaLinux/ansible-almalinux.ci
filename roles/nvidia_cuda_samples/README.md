# almalinux.ci.nvidia_cuda_samples

An Ansible role that installs Nvidia
[CUDA samples](https://github.com/NVIDIA/cuda-samples/).


## Role Variables

The role variables and their default values are listed below:

* `nvidia_cuda_samples_version: ''` - (**required**) CUDA samples version
  (e.g. 11.6).
* `nvidia_cuda_version: ''` - (**required**) a CUDA toolkit version (e.g. 11-6).
  This variable is used by the `almalinux.ci.nvidia_cuda` role.


## License

MIT


## Authors

* [Eugene Zamriy](https://github.com/ezamriy)
