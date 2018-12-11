import re
import os
import gi
import pycountry
gi.require_version('Notify', '0.7')
from gi.repository import Notify as notify


class Utils(object):
    # def __init__(self):
        # print('init utils')

    def cleanNotification(self, str):
        cleanStr = re.sub('[|/-]', '', str)
        cleanStr = re.sub('\\\\', '', cleanStr)
        tmpStrList = cleanStr.strip().splitlines(True)
        cleanStr = "".join([s for s in tmpStrList if s.strip()])
        return cleanStr

    def showNotification(self, title, message, imgPath=os.path.abspath('./resources/icons/nordvpn_icon_square.png')):
        """Shows balloon notification with given title and message"""
        notify.Notification.new("NordVPN - %s" % title, message, imgPath).show()

    def getCountryFlag(self, nordvpnCountry):
        countryStr = re.sub('_', ' ', nordvpnCountry)
        country = pycountry.countries.get(name=countryStr)
        countryCode = country.alpha_2
        flagPath = os.path.abspath('./resources/icons/countries/png/' + countryCode.lower() + '.png')
        return flagPath
