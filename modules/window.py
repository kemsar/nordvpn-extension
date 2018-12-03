#!/usr/bin/python2

import sys
import os
import signal
import threading
import time
import gi
import subprocess
from gi.repository import Gtk
from gi.repository import AppIndicator3 as appindicator
from gi.repository import Notify as notify
from xdg import DesktopEntry
from xdg import IconTheme
from functools import partial
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
gi.require_version('Notify', '0.7')

buttons = ["./resources/icons/auth_983008.png"]
iconSize = [48, 48]


class Window(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="NordVPN")
        # self.buttons=[];
        self.setupWindow()

    def setupWindow(self):
        self.set_border_width(10)

        box_outer = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(box_outer)

        listbox = Gtk.ListBox()
        listbox.set_selection_mode(Gtk.SelectionMode.NONE)
        box_outer.pack_start(listbox, True, True, 0)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        hbox.pack_start(vbox, True, True, 0)
        label = Gtk.Label("Auto-connect", xalign=0)
        vbox.pack_start(label, True, True, 0)
        switchAutoConnect = Gtk.Switch()
        switchAutoConnect.props.valign = Gtk.Align.CENTER
        hbox.pack_start(switchAutoConnect, False, True, 0)
        listbox.add(row)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        hbox.pack_start(vbox, True, True, 0)
        label = Gtk.Label("Auto-reconnect", xalign=0)
        vbox.pack_start(label, True, True, 0)
        switchAutoReConnect = Gtk.Switch()
        switchAutoReConnect.props.valign = Gtk.Align.CENTER
        hbox.pack_start(switchAutoReConnect, False, True, 0)
        listbox.add(row)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        hbox.pack_start(vbox, True, True, 0)
        label = Gtk.Label("Killswitch", xalign=0)
        vbox.pack_start(label, True, True, 0)
        switchKillswitch = Gtk.Switch()
        switchKillswitch.props.valign = Gtk.Align.CENTER
        hbox.pack_start(switchKillswitch, False, True, 0)
        listbox.add(row)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        hbox.pack_start(vbox, True, True, 0)
        label = Gtk.Label("CyberSec", xalign=0)
        vbox.pack_start(label, True, True, 0)
        switchCyberSec = Gtk.Switch()
        switchCyberSec.props.valign = Gtk.Align.CENTER
        hbox.pack_start(switchCyberSec, False, True, 0)
        listbox.add(row)

        # move the window to the cursor
        # pos = QtGui.QCursor().pos();
        # self.move(pos.x()-(iconSize[0]/2), pos.y()-iconSize[1]/2);
        self.show()

    def buttonClicked(self, button):
        os.system(execName + " &");
        # sys.exit();
