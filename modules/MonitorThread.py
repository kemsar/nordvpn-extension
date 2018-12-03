#!/usr/bin/python2

import sys
import os
import signal
import threading
import time
import gi
import subprocess
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
gi.require_version('Notify', '0.7')
from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator
from gi.repository import Notify as notify
from xdg import DesktopEntry;
from xdg import IconTheme;
from functools import partial;


class MonitorThread(object):
    """ Threading example class
    The run() method will be started and it will run in the background
    until the application exits.
    """

    def __init__(self, indicator, notifier, interval=10):
        """ Constructor
        :type interval: int
        :param interval: Check interval, in seconds
        """
        self.interval = interval
        self.indicator = indicator
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True                            # Daemonize thread
        notify.Notification.new("NordVPN - Activate", "The NordVPN daemon is running", None).show()
        thread.start()                                  # Start the execution

    def run(self):
        """ Method that runs forever """
        while True:
            # Do something
            # print('Doing something imporant in the background')

            result = subprocess.check_output(['nordvpn','status'])
            print(result)
            # self.indicator.get_menu()
            if "Disconnected" in result:
                self.indicator.set_icon(os.path.abspath('./resources/icons/nordvpn_icon_red.png'));
            else:
                self.indicator.set_icon(os.path.abspath('./resources/icons/nordvpn_icon_green.png'));
            time.sleep(self.interval)
