import requests
import re
page = requests.get("http://hageveld.mwp.nl/rooster/dagrooster/Ver_Kla.htm").text
ro = page.find(">6v<")
if ro == -1:
    roosterwijziging = "false"
else:
    roosterwijziging = "true"
print 'Klas 6v: ' + roosterwijziging
#print ro
