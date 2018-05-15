import servicemanager
import socket
import os
import sys
import win32event
import win32service
import win32serviceutil
import json
import logging
import logging.handlers
from pathlib import Path
import sys
import logging
import winreg
from a911 import Active911Client


# Load hidden modules for pyinstaller

import sleekxmpp.features.feature_bind
import sleekxmpp.features.feature_mechanisms
import sleekxmpp.features.feature_preapproval
import sleekxmpp.features.feature_rosterver
import sleekxmpp.features.feature_session
import sleekxmpp.features.feature_starttls

import sleekxmpp.plugins.xep_0030
import sleekxmpp.plugins.xep_0004
import sleekxmpp.plugins.xep_0060
import sleekxmpp.plugins.xep_0082
import sleekxmpp.plugins.xep_0131
import sleekxmpp.plugins.xep_0199



class WoodrowWilsonBridge(win32serviceutil.ServiceFramework):
    _svc_name_ = "WWBridge"
    _svc_display_name_ = "Woodrow Wilson Bridge"
    _svc_description_ = "Active 911 Client that generates json dumps of alert messages"

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        socket.setdefaulttimeout(60)

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)
        logging.info("Stopping Service...")

    def SvcDoRun(self):
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

        # Check if the config file exists, if it does read it in
        # Otherwise exit
        if Path(cf).exists():
            with open(cf, 'r') as cfh:
                opts = json.load(cfh);
        else:
            sys.exit('Unable to open config file "' + cd + '".')

        # Get Log Path from config file... if not found, default to 'log'
        lp = opts.get('logpath', 'log')

        # Check to see if the log path is relative or absoulte...
        # if relative path, add the config directory (cd) to the path
        if not os.path.splitdrive(lp)[0]:
            lp = os.path.join(cd, lp)

        # If log directory DNE create it
        if not os.path.exists(lp):
            os.makedirs(lp)

        # Get the output folder from config file... if not found, defautl to 'out'
        op = opts.get('outputpath', 'out')

        # Check to see if the out path is relative or absoulte...
        # if relative add the config directory (cd) to the path
        if not os.path.splitdrive(op)[0]:
            op = os.path.join(cd, op)

        # If output directory DNE, create it
        if not os.path.exists(op):
            os.makedirs(op)

        # Setup rotating logs
        rlh = logging.handlers.TimedRotatingFileHandler(
                                            os.path.join(lp, 'wwb_a911.log'), 
                                            when='midnight')
        
        # Logging begins here... is this not the most exciting thing ever
        # FYI we default to logging for info
        logging.basicConfig(level=int(opts.get('loglevel', logging.INFO)),
                            format='%(asctime)s %(levelname)-8s %(message)s',
                            datefmt='%H:%M:%S',
                            handlers=[rlh])

        logging.info("Starting up service.")
        logging.info("Output directory set to: %s." % op)
        logging.info("Logging directory set to: %s." % lp)

        xmpp = Active911Client(opts.get('a911_registration_id',''), op)

        # Connect to the XMPP server and start processing XMPP stanzas.
        if xmpp.connect():
            xmpp.process(block=True)
        else:
            logging.error("Unable to connect to Active911.")




if __name__ == '__main__':
    if len(sys.argv) == 1:
        servicemanager.Initialize()
        servicemanager.PrepareToHostSingle(WoodrowWilsonBridge)
        servicemanager.StartServiceCtrlDispatcher()
    else:
        win32serviceutil.HandleCommandLine(WoodrowWilsonBridge)