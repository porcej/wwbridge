# wwbridge

A Servie to connect to Active911 and export alert messages to
a predefined directory


## Prerequisites

This module is designed to work with `Python >=3.5`.  `Python 2` may work, your milage may very.  The `requirements.txt` file contains the required libraries.  

```
python >=  3.5
$pip install -r requirements.txt
```
## Building wwbridge

We will use pyinstaller to build an executable.  This will export the executable to the dist folder within the project directory

```

pyinstaller -F --hidden-import=win32timezone wwbridge.py
pyinstaller -F --hidden-import=win32timezone config.py

```

## Usage

Use config to generate json config file

```
Usage: 'wwbridge.exe [options] install|update|remove|start [...]|stop|restart [...]|debug [...]'
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
$dist\wwbridge.exe install
Installing service TestService
Service installed
```

### Start
```
$dist\wwbridge.exe start
Starting service TestService
```

### Clean
```
$dist\wwbridge.exe stop
$dist\wwbridge.exe remove
```

## Built With

* [Anaconda Python](https://conda.io/) - The python framework
* [SleekXMPP](https://github.com/fritzy/SleekXMPP) - XMPP Library
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
