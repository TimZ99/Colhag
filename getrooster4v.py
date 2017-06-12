import requests
page = requests.get("http://hageveld.mwp.nl/rooster/dagrooster/Ver_Kla.htm").text
ro = page.find(">4v<")
if ro == -1:
    roosterwijziging = "false"
else:
    roosterwijziging = "true"
print 'Klas 4v: ' + roosterwijziging
#print ro
