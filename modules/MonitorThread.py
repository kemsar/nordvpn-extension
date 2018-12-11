#!/usr/bin/python2

import os
import threading
import time
import subprocess
import ConfigParser
import StringIO
from modules.Utils import Utils
# from modules.Config import Config

utils = Utils()
# config = Config()


class MonitorThread(object):
    """ Threading example class
    The run() method will be started and it will run in the background
    until the application exits.
    """

    def __init__(self, indicator, interval=10):
        """ Constructor
        :type interval: int
        :param interval: Check interval, in seconds
        """
        self.interval = interval
        self.indicator = indicator
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True                            # Daemonize thread
        utils.showNotification('Activated', 'The NordVPN daemon is running')
        thread.start()                                  # Start the execution

    def run(self):
        """ Method that runs forever """
        while True:

            result = subprocess.check_output(['nordvpn', 'status'])
            status = ConfigParser.ConfigParser()
            str = '[Default]\r\n'
            ini = str + utils.cleanNotification(result)
            buf = StringIO.StringIO(ini)
            status.readfp(buf)
            # self.indicator.get_menu()
            if "Disconnected" in result:
                iconPath = './resources/icons/nordvpn_icon_square.png'
                path = os.path.abspath(iconPath)
                self.indicator.set_icon(path)
            else:
                iconPath = utils.getCountryFlag(status.get('Default','Country'))
                path = os.path.abspath(iconPath)
                self.indicator.set_icon(path)
            time.sleep(self.interval)
