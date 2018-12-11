import ConfigParser
import os
import subprocess
import StringIO
from modules.Utils import Utils


class Config(object):

    def __init__(self, iniPath=os.path.abspath('./resources/config.ini')):
        self.iniPath = iniPath
        self.parser = ConfigParser.ConfigParser()
        self.parser.read(self.iniPath)
        # TODO: read settings from nordvpn and update to/from (?) config file
        result = subprocess.check_output(['nordvpn', 'settings'])
        settings = ConfigParser.ConfigParser()
        str = '[Default]\r\n'
        ini = str + Utils().cleanNotification(result)
        buf = StringIO.StringIO(ini)
        settings.readfp(buf)
        self.setProtocol(settings.get('Default', 'Protocol'))
        self.setKillswitch(settings.get('Default', 'Kill Switch'))
        self.setCybersec(settings.get('Default', 'CyberSec'))
        self.setObfuscate(settings.get('Default', 'Obfuscate'))
        self.setAutoconnect(settings.get('Default', 'Auto connect'))

    def booleanValue(self, setting):
        param = self.parser.get('Default', setting).lower()
        if (param == 'true'):
            return True
        elif (param == 'enabled'):
            return True
        else:
            return False

    def killswitchIsEnabled(self):
        return (self.booleanValue('killswitch'))

    def cybersecIsEnabled(self):
        return (self.booleanValue('cybersec'))

    def reconnectIsEnabled(self):
        return (self.parser.getboolean('Default', 'reconnect'))

    def autoconnectIsEnabled(self):
        return (self.booleanValue('autoconnect'))

    def obfuscateIsEnabled(self):
        return (self.booleanValue('obfuscate'))

    def getCountry(self):
        return self.parser.get('Default', 'country')

    def getProtocol(self):
        return self.parser.get('Default', 'protocol')

    def setProtocol(self, protocol):
        self.parser.set('Default', 'protocol', protocol)
        self.save()
        result = subprocess.check_output(['nordvpn', 'set', 'protocol', protocol])
        print(result)

    def setCountry(self, country):
        self.parser.set('Default', 'country', country)
        self.save()

    def setObfuscate(self, obfuscate):
        self.parser.set('Default', 'obfuscate', obfuscate)
        self.save()
        result = subprocess.check_output(['nordvpn', 'set', 'obfuscate', str(obfuscate).lower()])
        print(result)

    def setAutoconnect(self, autoconnect):
        self.parser.set('Default', 'autoconnect', autoconnect)
        self.save()
        result = subprocess.check_output(['nordvpn', 'set', 'autoconnect', str(autoconnect).lower()])
        print(result)

    def setReconnect(self, reconnect):
        self.parser.set('Default', 'reconnect', reconnect)
        self.save()

    def setCybersec(self, cybersec):
        self.parser.set('Default', 'cybersec', cybersec)
        self.save()
        result = subprocess.check_output(['nordvpn', 'set', 'cybersec', str(cybersec).lower()])
        print(result)

    def setKillswitch(self, killswitch):
        self.parser.set('Default', 'killswitch', killswitch)
        self.save()
        result = subprocess.check_output(['nordvpn', 'set', 'killswitch', str(killswitch).lower()])
        print(result)

    def save(self):
        with open(self.iniPath, 'w') as configfile:
            self.parser.write(configfile)
