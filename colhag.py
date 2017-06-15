# -*- coding: utf-8 -*-

# Import
import time
import telepot
import urllib2
import json
from telepot.loop import MessageLoop
print "\n"

# Import token
import token

# Getrooster for all classes
import getrooster1v
import getrooster2v
import getrooster3v
import getrooster4v
import getrooster5v
import getrooster6v

# Check if getrooster is true, if so show url to website
def rooster(klas, chatid):
    if getrooster1v.roosterwijziging == "true" and klas == "1v":
        bot.sendMessage(chatid, """\
    Er is een roosterwijziging!
    http://hageveld.mwp.nl/rooster/dagrooster/Ver_Kla_1v.htm
    """)
    elif getrooster2v.roosterwijziging == "true":
        bot.sendMessage(chatid, """\
    Er is een roosterwijziging!
    http://hageveld.mwp.nl/rooster/dagrooster/Ver_Kla_2v.htm
    """)
    elif getrooster3v.roosterwijziging == "true":
        bot.sendMessage(chatid, """\
    Er is een roosterwijziging!
    http://hageveld.mwp.nl/rooster/dagrooster/Ver_Kla_3v.htm
    """)
    elif getrooster4v.roosterwijziging == "true":
        bot.sendMessage(chatid, """\
    Er is een roosterwijziging!
    http://hageveld.mwp.nl/rooster/dagrooster/Ver_Kla_4v.htm
    """)
    elif getrooster5v.roosterwijziging == "true":
        bot.sendMessage(chatid, """\
    Er is een roosterwijziging!
    http://hageveld.mwp.nl/rooster/dagrooster/Ver_Kla_5v.htm
    """)
    elif getrooster6v.roosterwijziging == "true":
        bot.sendMessage(chatid, """\
    Er is een roosterwijziging!
    http://hageveld.mwp.nl/rooster/dagrooster/Ver_Kla_6v.htm
    """)
    else:
        bot.sendMessage(chatid, """\
    Er zijn geen roosterwijzigingen!
    """)

# Handle Commands
def handle(msg):
    # Check is message is location, text of something else
	com = 1
	lo = 1
	try:
		msg['location']['longitude']
	except KeyError:
		lo = None
	try:
		msg['text']
	except KeyError:
		com = None

	if lo is None and com is None:
		command = "Not a location or text"
	elif lo is not None:
		lon = "%.9f" % msg['location']['longitude']
		lat = "%.9f" % msg['location']['latitude']
		command = "Sending locatie lon: "+lon+" Lat: "+lat
	else:
		command = msg['text']

    # Print command in terminal
	print 'Got command: %s' % command

    # Get chat id
	chat_id = msg['chat']['id']

    # Handle '/start'
	if(command == '/start'):
		bot.sendMessage(chat_id, """
Hoi, ik ben Colhag en ik ben een bot.
Ik kan je het weer laten zien en kijken of je klas een roosterwijziging heeft.
Weten hoe het werkt of heb je vragen? Typ '/help'.

Wil je weten door wie ik gemaakt ben? Typ '/credits', doe maar, is leuk ;).
""")
    # Handle '/help'
	elif(command == '/help'):
		bot.sendMessage(chat_id, """
Commando's om mij te besturen zijn:
/start Dit heb je al gedaan, maar ik wil je best nog eens begroeten
/help Dit bericht :)
/credits Je moet natuurlijk wel weten door wie ik gemaakt ben
/hoi Gewoon even om hoi te zeggen
/rooster Bekijk of er roosterwijzigingen zijn
/weer Bekijk de weersvoorspelling
""")
    # Handle '/credits'
	elif(command == '/credits'):
		bot.sendMessage(chat_id, """
En de credits gaaaaan naaaaar... (trommelgeroffel)

Code > Tim
Getest door > Jaxon
Code herschreven door Tim en @hous3m4ster, nu crash ik tenminste niet meer (zo vaak) :P
""")
    # Handle '/hoi'
	elif(command == '/hoi'):
		bot.sendMessage(chat_id, 'Hoi!')

    # Handle '/rooster'
	elif('/rooster' in command):

        #TODO
        # Add custom Keyboard

        # Show is there is a change per class
		if command == "/rooster 6v":
			rooster("6v", chat_id)
		elif command == "/rooster 6V":
			rooster("6v", chat_id)

		elif command == "/rooster 5v":
			rooster("5v", chat_id)
		elif command == "/rooster 5V":
			rooster("5v", chat_id)

		elif command == "/rooster 4v":
			rooster("4v", chat_id)
		elif command == "/rooster 4V":
			rooster("4v", chat_id)

		elif command == "/rooster 3v":
			rooster("3v", chat_id)
		elif command == "/rooster 3V":
			rooster("3v", chat_id)

		elif command == "/rooster 2v":
			rooster("2v", chat_id)
		elif command == "/rooster 2V":
			rooster("2v", chat_id)

		elif command == "/rooster 1v":
			rooster("1v", chat_id)
		elif command == "/rooster 1V":
			rooster("1v", chat_id)

        # If no class is specified print all classes
		else:
			bot.sendMessage(chat_id, "Klas 1v")
			rooster("1v", chat_id)
			bot.sendMessage(chat_id, "Klas 2v")
			rooster("2v", chat_id)
			bot.sendMessage(chat_id, "Klas 3v")
			rooster("3v", chat_id)
			bot.sendMessage(chat_id, "Klas 4v")
			rooster("4v", chat_id)
			bot.sendMessage(chat_id, "Klas 5v")
			rooster("5v", chat_id)
			bot.sendMessage(chat_id, "Klas 6v")
			rooster("6v", chat_id)
			bot.sendMessage(chat_id, "Om voortaan alleen jouw klas te zien dien je '/rooster (jouw klas)' te typen.")
			bot.sendMessage(chat_id, "/mijnklasstaaternietbij")

    # Handle '/mijnklasstaaternietbij'
	elif(command == '/mijnklasstaaternietbij'):
		bot.sendMessage(chat_id, "Deze functie werk momenteel alleen voor VIA klassen. Staat jouw (reguliere) klas er niet bij? Stuur dan even een mail naar Tim@Xervion.nl en misschien voegen we jouw klas wel toe ;).")

    # Handle '/weer'
	elif(command == '/weer'):
		bot.sendMessage(chat_id, """\
Stuur je locatie!
(Dit werkt niet in groepen!)
""")
    # Handle 'location' and show weather
	elif(lo is not None):
		json_obj=urllib2.urlopen('http://api.openweathermap.org/data/2.5/weather?lat='+lat+'&lon='+lon+'&appid=d89ab85c7700a2ee6e26475397209c20')
		data=json.load(json_obj)
		for i in data['weather']:
			if i['main']=='Rain':
			    bot.sendMessage(chat_id, "Kut! Het regent weer!")
		K=data['main']['temp']
		celsius=K-273.15
		if celsius>20:
			bot.sendMessage(chat_id, "Het is lekker!")
		elif celsius>5 and celsius<20:
			bot.sendMessage(chat_id, "Het is een beetje matig weer, het is niet warm, het is niet koud!")
		elif celsius<5:
			bot.sendMessage(chat_id, "Het is koud!")
		celsius = "%.1f" % celsius
		bot.sendMessage(chat_id, "Het is "+celsius+" graden.")


bot = telepot.Bot(token.API_TOKEN)

MessageLoop(bot, handle).run_as_thread()
print ('Listening ... \n')

while(1):
	time.sleep(10)
