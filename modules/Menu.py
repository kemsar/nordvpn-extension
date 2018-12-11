import gi
import subprocess
import os
from modules.Utils import Utils
# from modules.Config import Config
from modules.Window import Window
gi.require_version('Gtk', '3.0')
gi.require_version('Notify', '0.7')
from gi.repository import Gtk, Notify


class Menu(Gtk.Menu):

    def __init__(self, config):
        Gtk.Menu.__init__(self)
        self.utils = Utils()
        self.config = config
        item_status = Gtk.MenuItem('Status')
        item_login = Gtk.MenuItem('Login')
        item_connect = Gtk.MenuItem('Connect')
        item_disconnect = Gtk.MenuItem('Disconnect')
        item_display = Gtk.MenuItem('Settings')
        item_logout = Gtk.MenuItem('Logout')
        item_quit = Gtk.MenuItem('Quit')
        item_status.connect('activate', self.status)
        item_login.connect('activate', self.login)
        item_logout.connect('activate', self.logout)
        item_display.connect('activate', self.display)
        item_connect.connect('activate', self.connect)
        item_disconnect.connect('activate', self.disconnect)
        item_quit.connect('activate', quit)
        self.append(item_status)
        self.append(item_login)
        self.append(item_logout)
        self.append(item_connect)
        self.append(item_disconnect)
        self.append(item_display)
        self.append(item_quit)
        self.show_all()

    def status(self, source):
        result = subprocess.check_output(['nordvpn', 'status'])
        self.utils.showNotification("Status", self.utils.cleanNotification(result))

    def login(self, source):
        os.system("gnome-terminal -e 'nordvpn login'")

    def logout(self, source):
        result = subprocess.check_output(['nordvpn', 'logout'])
        self.utils.showNotification("Logout", self.utils.cleanNotification(result))
        print(result)

    def connect(self, source):
        args = ['nordvpn', 'connect', self.config.getCountry()]
        result = subprocess.check_output(args)
        self.utils.showNotification("Connect", self.utils.cleanNotification(result))
        print(result)

    def disconnect(self, source):
        result = subprocess.check_output(['nordvpn', 'disconnect'])
        self.utils.showNotification("Disconnect", self.utils.cleanNotification(result))
        print(result)

    def display(self, source):
        win = Window(self.config)
        win.show_all()

    def quit(self, source):
        Notify.uninit()
        Gtk.main_quit()
