# wwbridge

A Servie to connect to Active911 and export alert messages to
a predefined directory


## Prerequisites

This module is designed to work with `Python 3.4+` on a `Windows` system.  `Python 2` may work, your milage may very.  The `requirements.txt` file contains the required libraries except for a911client and optionally sleekmonkey.  

```
python 3.4+
$ pip install -r requirements.txt
$ mkdir a911-build
$ cd a911-build
$ git clone https://github.com/porcej/a911client
$ cd a911client
$ python setup.py install

# The following is optional, to install sleekmonkey
$ cd ..
$ git clonge https://github.com/porcej/sleekmonkey
$ cd sleekmonkey
$ python setup.py install

# The following is optional to remove a911client's build directory
$ cd ..\..
$ cd rm -rf a911-build

```
## Building wwbridge

We will use pyinstaller to build an executable.  This will export the executable to the dist folder within the project directory

```

pyinstaller -F --hidden-import=win32timezone ww_bridge.py
pyinstaller -F --hidden-import=win32timezone config.py

```

## Usage

Use config to generate json config file

```
Usage: 'ww_bridge.exe [options] install|update|remove|start [...]|stop|restart [...]|debug [...]'
Options for 'install' and 'update' commands only:
 --username domain\username : The Username the service is to run under
 --password password : The password for the username
 --startup [manual|auto|disabled|delayed] : How the service starts, default = manual
 --interactive : Allow the service to interact with the desktop.
 --perfmonini file: .ini file to use for registering performance monitor data
 --perfmondll file: .dll file to use when querying the service for
   performance data, default = perfmondata.dll
Options for 'start' and 'stop' commands only:
 --wait seconds: Wait for the service to actually start or stop.
                 If you specify --wait with the 'stop' option, the service
                 and all dependent services will be stopped, each waiting
                 the specified period.
```

### Install
```
$dist\ww_bridge.exe install
Installing service TestService
Service installed
```

### Start
```
$dist\ww_bridge.exe start
Starting service TestService
```

### Clean
```
$dist\ww_bridge.exe stop
$dist\ww_bridge.exe remove
```

## Built With

* [Anaconda Python](https://conda.io/) - The python framework
* [SleekXMPP](https://github.com/fritzy/SleekXMPP) - XMPP Library
* [A911Client](https://github.com/porcej/a911client) - Active 911 Alert Client
* [SleekMonkey](https://github.com/porcej/sleekmonkey) - Patch for SleekXMPP 1.3.3 to better handle TLS Certificate dates
* [Requests](http://docs.python-requests.org/en/master/) - Request and session handling

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/porcej/cc71497a2b455f27bca8c879731e68dc) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/porcej/a911_bridge/tags). 

## Authors

* **Joseph Porcelli** - *Initial work* - [porcej](https://github.com/porcej)

See also the list of [contributors](https://github.com/porcej/a911_bridge/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
