import requests
page = requests.get("http://hageveld.nl/rooster/dagrooster/Ver_Kla.htm").text
ro = page.find(">1v<")
if ro == -1:
    roosterwijziging = "false"
else:
    roosterwijziging = "true"
print ('Klas 1v: ' + roosterwijziging)
