#!/usr/bin/env python
# -*- coding: ascii -*-

"""
A really simple configuration manager for
Woodrow Wilson Bridge
"""

__author__ = "Joseph Porcelli (porcej@gmail.com)"
__version__ = "0.0.1"
__copyright__ = "Copyright (c) 2018 Joseph Porcelli"
__license__ = "MIT"

import os
import sys
import json
import winreg
from pathlib import Path

if sys.version_info < (3, 0):
    reload(sys)
    sys.setdefaultencoding('utf8')
else:
    raw_input = input

if __name__ == '__main__':
    opts = {}
    importantKeys = {
                        'logpath' : 'Please enter logging path', 
                        'outputpath': 'Please enter the output path', 
                        'a911_registration_id': 'Please enter your Active911 Device ID', 
                        'loglevel': 'Please Provide a logging level integer (WARNING=30, INFO=20, DEBUG=10, VERBOSE=0)'
                    }

    # Config directory - default to c:\\ww_bridge
    cd = 'C:\\ww_bridge'
    # Check the registry to see if there is a better config directory
    try:
        regKey = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\Porcej\wwbridge')
        regVal = winreg.QueryValueEx(regKey, r'Path')
        if regVal[0]:
            cd = regVal[0]
    except:
        # Don't worry if we have an error here, we have already set the default path
        # so here we do nothing and that is fine.
        pass    

    # Join the config file name config.json to the config path        
    cf = os.path.join(cd, 'config.json')

    print("Loading configuration file: %s" % cf)

    # Check if the config file exists, if it does read it in
    # Otherwise exit
    if Path(cf).exists():
        with open(cf, 'r') as cfh:
            opts = json.load(cfh);
    else:
        sys.exit('Unable to open config file "' + cd + '".')

    for key, prompt in importantKeys.items():
        if key in opts:
            opts[key] = raw_input("%s[%s]:" % (prompt, opts[key])) or opts[key]
        else:
            opts[key] = raw_input("%s:" % prompt)

    # Write config.json
    with open(cf, 'w') as cfh:
        json.dump(opts, cfh, sort_keys=True, indent=4)

