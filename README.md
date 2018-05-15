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

```

## Usage

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