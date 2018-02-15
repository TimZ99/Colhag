import requests
page = requests.get("http://hageveld.nl/rooster/dagrooster/Ver_Kla.htm").text
ro = page.find(">5v<")
if ro == -1:
    roosterwijziging = "false"
else:
    roosterwijziging = "true"
print ('Klas 5v: ' + roosterwijziging)
