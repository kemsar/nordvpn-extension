#!/usr/bin/python2

import gi
import subprocess
from modules.Utils import Utils
# from modules.Config import Config
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

buttons = ["./resources/icons/auth_983008.png"]
iconSize = [48, 48]
utils = Utils()


class Window(Gtk.Window):
    def __init__(self, config):
        Gtk.Window.__init__(self, title="NordVPN")
        # self.buttons=[];
        self.settings = config
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
        label = Gtk.Label("Auto-Connect", xalign=0)
        vbox.pack_start(label, True, True, 0)
        switchAutoConnect = Gtk.Switch()
        switchAutoConnect.set_active(self.settings.autoconnectIsEnabled())
        switchAutoConnect.connect("notify::active", self.onAutoconnectActivated)
        switchAutoConnect.props.valign = Gtk.Align.CENTER
        hbox.pack_start(switchAutoConnect, False, True, 0)
        listbox.add(row)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        hbox.pack_start(vbox, True, True, 0)
        label = Gtk.Label("Auto-Reconnect", xalign=0)
        vbox.pack_start(label, True, True, 0)
        switchAutoReConnect = Gtk.Switch()
        switchAutoReConnect.set_active(self.settings.reconnectIsEnabled())
        switchAutoReConnect.connect("notify::active", self.onReconnectActivated)
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
        switchKillswitch.set_active(self.settings.killswitchIsEnabled())
        switchKillswitch.connect("notify::active", self.onKillswitchActivated)
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
        switchCyberSec.set_active(self.settings.cybersecIsEnabled())
        switchCyberSec.connect("notify::active", self.onCybersecActivated)
        switchCyberSec.props.valign = Gtk.Align.CENTER
        hbox.pack_start(switchCyberSec, False, True, 0)
        listbox.add(row)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        hbox.pack_start(vbox, True, True, 0)
        label = Gtk.Label("Obfuscate", xalign=0)
        vbox.pack_start(label, True, True, 0)
        switchObfuscate = Gtk.Switch()
        switchObfuscate.set_active(self.settings.obfuscateIsEnabled())
        switchObfuscate.connect("notify::active", self.onObfuscateActivated)
        switchObfuscate.props.valign = Gtk.Align.CENTER
        hbox.pack_start(switchObfuscate, False, True, 0)
        listbox.add(row)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        hbox.pack_start(vbox, True, True, 0)
        label = Gtk.Label("Protocol", xalign=0)
        vbox.pack_start(label, True, True, 0)

        udpButton = Gtk.RadioButton.new_with_label_from_widget(None, 'UDP')
        udpButton.connect("toggled", self.onProtocolToggled, 'UDP')
        hbox.pack_start(udpButton, False, False, 0)

        tcpButton = Gtk.RadioButton.new_from_widget(udpButton)
        tcpButton.set_label("TCP")
        tcpButton.connect("toggled", self.onProtocolToggled, 'TCP')
        hbox.pack_start(tcpButton, False, False, 0)

        if(self.settings.getProtocol() == 'TCP'):
            tcpButton.set_active(True)
        else:
            udpButton.set_active(True)

        listbox.add(row)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        hbox.pack_start(vbox, True, True, 0)
        label = Gtk.Label("Country", xalign=0)
        vbox.pack_start(label, True, True, 0)
        country_combo = Gtk.ComboBoxText()
        country_combo.connect("changed", self.on_country_combo_changed)
        country_combo.set_entry_text_column(0)
        result = subprocess.check_output(['nordvpn', 'countries'])
        countryIndex = -1
        selectCountryIndex = -1
        for country in sorted(result.split()):
            countryIndex = countryIndex+1
            if (country == self.settings.getCountry()):
                selectCountryIndex = countryIndex
            country_combo.append_text(country)
        country_combo.set_active(selectCountryIndex)
        country_combo.props.valign = Gtk.Align.CENTER
        hbox.pack_start(country_combo, False, True, 0)
        listbox.add(row)

        # move the window to the cursor
        # pos = QtGui.QCursor().pos();
        # self.move(pos.x()-(iconSize[0]/2), pos.y()-iconSize[1]/2);
        self.show()

    def on_country_combo_changed(self, combo):
        text = combo.get_active_text()
        if text is not None:
            self.settings.setCountry(text)

    def onAutoconnectActivated(self, switch, gparam):
        self.settings.setAutoconnect(switch.get_active())

    def onKillswitchActivated(self, switch, gparam):
        self.settings.setKillswitch(switch.get_active())

    def onCybersecActivated(self, switch, gparam):
        self.settings.setCybersec(switch.get_active())

    def onReconnectActivated(self, switch, gparam):
        self.settings.setReconnect(switch.get_active())

    def onObfuscateActivated(self, switch, gparam):
        self.settings.setObfuscate(switch.get_active())

    def onProtocolToggled(self, button, name):
        if(button.get_active()):
            self.settings.setProtocol(name)
