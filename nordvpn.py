#!/usr/bin/python2

import os
import signal
import gi
from modules.MonitorThread import MonitorThread
from modules.Utils import Utils
from modules.Config import Config
from modules.Menu import Menu
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
gi.require_version('Notify', '0.7')
from gi.repository import Gtk, AppIndicator3, Notify

APPINDICATOR_ID = 'NordVPN_appIndicator'
signal.signal(signal.SIGINT, signal.SIG_DFL)
utils = Utils()
config = Config(os.path.abspath('./resources/config.ini'))


def main():

    path = os.path.abspath('./resources/icons/nordvpn_icon_square.png')
    category = AppIndicator3.IndicatorCategory.SYSTEM_SERVICES
    indicator = AppIndicator3.Indicator.new(APPINDICATOR_ID, path, category)
    indicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)
    indicator.set_menu(Menu(config))
    Notify.init("NordVPN")
    MonitorThread(indicator, 20)
    Gtk.main()


if __name__ == '__main__':
    main()
