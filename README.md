# OMI Python Script Provider [![Build Status](https://travis-ci.org/Microsoft/omi-script-provider.svg?branch=master)](https://travis-ci.org/Microsoft/omi-script-provider)


### Additional Resources

- [Script Provider Getting Started Guide](/doc/gettingStarted.md)

### Supported Linux Operating Systems

We support most Linux platforms which support python2.7 by default. That
said, our formal tested matrix of Linux platforms includes the following:

- CentOS 7 x64
- Debian 7, 8 (x86 and x64) and Debian 9 x64
- Oracle Linux 7 x64
- Red Hat Enterprise Linux Server 7 x64
- SUSE Linux Enteprise Server 12 x64
- Ubuntu 12.04 LTS, 14.04 LTS, and 16.04 LTS (x86 and x64)

### How to build

#### Dependencies to build OMI Python Script Provider:

Before you build OMI Python Script Provider, you should check [OMI_Build_Dependencies](https://github.com/Microsoft/Build-omi#dependencies-to-build-a-native-package), then you can build the provider as following:

- Install python and python-devel
  - Redhat/CentOS: 
    ```
    sudo yum update
    sudo yum install python27 python27-devel
    ```
  - Debian/Ubuntu OS: 
    ```
    sudo apt-get update
    sudo apt-get install python2.7 python2.7-dev 
    ```
    Note: If you use old OS version like Ubuntu 12.04 or Ubuntu 14.04, you might need to run command:`sudo add-apt-repository ppa:fkrull/deadsnakes` to get python to be installed.

#### To clone the repository to build OMI Python Script Provider, issue the following commands:
```
git clone --recursive https://github.com/Microsoft/Build-omi-script-provider
cd Build-omi-script-provider/omi/Unix
./configure --dev
make -j
make install
cd ../../scriptprovider
./configure
make
sudo make install
```

### Developing an OMI Python Script Provider

To develop an OMI Python Script Provider, the [OMI](https://github.com/Microsoft/omi) is required to be built in the developer mode.
Please refer to [How to build](https://github.com/Microsoft/omi-script-provider#how-to-build) in order to do that.

After building the project, we need to define "schema.mof" and to generate the Provider Sources from it.
We need to create first a directory under the lib directory of the OMI. For the developer build, this will be ```Build-omi-script-provider/omi/Unix/output/lib```. If the OMI was installed with a package, the root library location is ```/opt/omi/lib```. Replace the path with the one that applies for your environment, in our case will be the first one since we built it from source.
```
> cd Build-omi-script-provider/omi/Unix/output/lib
> mkdir XYZ_Frog
> cd XYZ_Frog
```
Example of "schema.mof" file:
```
class XYZ_Frog
{
 [Key] String Name;
 Uint32 Weight;
 String Color;
};
```

In order to generate the Provider Sources from the schema file, we need to run omigen_py:
```
> ../../../../../scriptprovider/output/bin/omigen_py schema.mof XYZ_Frog
Creating "schema.py"
Creating "mi_main.py"
```
The omigen_py tool will generate the files ```schema.py``` and ```mi_main.py```.

The file mi_main.py will be edited in order to implement the custom python provider.
Please refer to [Script Provider Getting Started Guide](/doc/gettingStarted.md) for more details.

We can now register the Python Provider using the omireg command:
```
> ../../bin/omireg --Python XYZ_Frog
Created /home/ubuntu/docs_update/Build-omi-script-provider/omi/Unix/output/etc/omiregister/root-cimv2/XYZ_Frog.reg
```


# Contributing

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.
