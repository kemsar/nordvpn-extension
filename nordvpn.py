#!/usr/bin/python2

# import sys
import os
# import signal
# import threading
# import time
import gi
import subprocess
import ConfigParser
from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator
from gi.repository import Notify as notify
# from PyQt4 import QtCore;
# from PyQt4 import QtGui;
# from xdg import DesktopEntry;
# from xdg import IconTheme;
# from functools import partial;
# from modules.MonitorThread import MonitorThread
from modules.window import Window
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
gi.require_version('Notify', '0.7')

APPINDICATOR_ID = 'myappindicator'
config = ConfigParser.RawConfigParser()

# class MonitorThread(object):
#     """ Threading example class
#     The run() method will be started and it will run in the background
#     until the application exits.
#     """
#
#     def __init__(self, interval=10):
#         """ Constructor
#         :type interval: int
#         :param interval: Check interval, in seconds
#         """
#         self.interval = interval
#
#         thread = threading.Thread(target=self.run, args=())
#         thread.daemon = True                            # Daemonize thread
#         thread.start()                                  # Start the execution
#
#     def run(self):
#         """ Method that runs forever """
#         while True:
#             # Do something
#             # print('Doing something imporant in the background')
#
#             result = subprocess.check_output(['nordvpn','status'])
#             print(result)
#             time.sleep(self.interval)


def build_menu():
    menu = gtk.Menu()
    item_status = gtk.MenuItem('Status')
    item_login = gtk.MenuItem('Login')
    item_connect = gtk.MenuItem('Connect')
    item_disconnect = gtk.MenuItem('Disconnect')
    item_display = gtk.MenuItem('Settings')
    item_logout = gtk.MenuItem('Logout')
    item_quit = gtk.MenuItem('Quit')
    item_status.connect('activate', status)
    item_login.connect('activate', login)
    item_logout.connect('activate', logout)
    item_display.connect('activate', display)
    item_connect.connect('activate', connect)
    item_disconnect.connect('activate', disconnect)
    item_quit.connect('activate', quit)
    menu.append(item_status)
    menu.append(item_login)
    menu.append(item_logout)
    menu.append(item_connect)
    menu.append(item_disconnect)
    menu.append(item_display)
    menu.append(item_quit)
    menu.show_all()
    return menu


def status(source):
    result = subprocess.check_output(['nordvpn', 'status'])
    _show_notification("Status", result)
    print(result)


def login(source):
    os.system("gnome-terminal -e 'nordvpn login'")


def logout(source):
    result = subprocess.check_output(['nordvpn', 'logout'])
    _show_notification("Logout", result)
    print(result)


def connect(source):
    result = subprocess.check_output(['nordvpn', 'connect'])
    _show_notification("Connect", result)
    print(result)


def disconnect(source):
    result = subprocess.check_output(['nordvpn', 'disconnect'])
    _show_notification("Disconnect", result)
    print(result)


def display(source):
    win = Window()
    win.show_all()


def quit(source):
    notify.uninit()
    gtk.main_quit()


def _show_notification(title, message):
    """Shows balloon notification with given title and message"""
    notify.Notification.new("NordVPN - %s" % title, message, None).show()


def main():
    """load config settings"""
    config.read("./resources/config.ini")

    # print config.sections()
    # print config.options('Settings')
    # print config.get('Settings','killswitch')

    path = os.path.abspath('./resources/icons/nordvpn_icon.png')
    category = appindicator.IndicatorCategory.SYSTEM_SERVICES
    indicator = appindicator.Indicator.new(APPINDICATOR_ID, path, category)
    indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
    indicator.set_menu(build_menu())

    notify.init("NordVPN")
    # bgThread = MonitorThread(indicator,notify,20)
    gtk.main()


if __name__ == '__main__':
    main()
