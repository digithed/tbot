#!/usr/bin/python2.7
import os
import time
import math
from slackclient import SlackClient
from playsound import playsound
import requests
from lxml import html
from twilio.rest import Client
from ast import literal_eval
from playsound import playsound


client = Client("AC7f381966d695e79d08f1338c4e3b6f99","e208e020508583645d521838cd596bd6")


page = requests.get('http://games.espn.com/ffl/leaders?&seasonTotals=true&seasonId=2017')
tree = html.fromstring(page.content)

players = tree.xpath('//td/a[@cache="true"]/text()')
stats = tree.xpath('//td[@class="playertableStat appliedPoints sortedCell"]/text()')
pArray = players[0:10]
sArray = stats[0:10]
newarray = []
newarray.append(pArray[0:1] + sArray[0:1])
newarray.append(pArray[1:2] + sArray[1:2])
newarray.append(pArray[2:3] + sArray[2:3])
newarray.append(pArray[3:4] + sArray[3:4])
newarray.append(pArray[4:5] + sArray[4:5])
newarray.append(pArray[5:6] + sArray[5:6])
newarray.append(pArray[6:7] + sArray[6:7])
newarray.append(pArray[7:8] + sArray[7:8])
newarray.append(pArray[8:9] + sArray[8:9])
newarray.append(pArray[9:10] + sArray[9:10])

newarray1 = [[s.strip() for s in inner] for inner in newarray]


page1 = requests.get('https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/ref=zg_bs_nav_0')
tree = html.fromstring(page1.content)

item = tree.xpath('//div[@data-truncate-mix-weblab="true"]/text()')
price = tree.xpath('//span[@class="p13n-sc-price"]/text()')

a = item[0:20]
b = price[0:20]
new = []

new.append(a[0:1] + b[0:1])
new.append(a[1:2] + b[1:2])
new.append(a[2:3] + b[2:3])
new.append(a[3:4] + b[3:4])
new.append(a[4:5] + b[4:5])

new1 = [[s.strip() for s in inner] for inner in new]

#notepad = []
#notepad_z = []
#notepad_m = [notepad_z,notepad]
text_file = open("notes.txt", "a")


test = []
x = []
#notepad_z.append(db.read())
#thingy = db.read()
BOT_ID = os.environ.get("BOT_ID")
nickid= '<@U7KF5HRNK>'
AT_BOT = "<@" + BOT_ID + ">"
commandlist = ["joke","max","bryan","tom","nick","rosenau","help","who","shutup","games","games switch","ok","top10","amazon","netflix","notes","~notes","#notes","sms","test","rotten","math"]

slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))

#def main():
sc = slack_client
bby = []
read = []
snapshot = open("names.txt", "r")
snaplen = snapshot.read()
b=0

rottenpage = requests.get("https://www.rottentomatoes.com/m/godfather")

rtree = html.fromstring(rottenpage.content)


score = rtree.xpath('//span[@class="meter-value superPageFontColor"]/span/text()')
consensus = rtree.xpath('//*[contains(@class, "critic_consensus superPageFontColor")]//text()')

z = ",".join(consensus[1:5])
y = "".join(score[0:1])
b = z.replace("   ", "")
final = "Score: " + y + "%"+ " | " + b



def handle_command(command, channel):
	"""
		Receives commands directed at the bot and determines if they
		are valid commands. If so, then acts on the commands. If not,
		returns back what it needs for clarification.
	"""
	
	signs = '+-*/'
	if command not in commandlist and (len(command) > 5 or len(command) < 5) and " " not in command and '+' not in command and '-' not in command and '*' not in command and '/' not in command:
		response = "Not sure what you mean. Use a *verified command* as listed through the 'help' command."
		slack_client.api_call("chat.postMessage", channel=channel,
						  text=response, as_user=True)

	if command.startswith(commandlist[0]):
		response = "Knock! Knock! Who's there? Banana. Banana who? But Nana said my name was Nick."
		slack_client.api_call("chat.postMessage", channel=channel,
						  text=response, as_user=True)
	if command.startswith(commandlist[1]):
		response1 = "Max is the oldest sibling in the Rosenau family :smile:"
		slack_client.api_call("chat.postMessage", channel=channel,
						  text=response1, as_user=True)
	if command.startswith(commandlist[2]):
		response1 = "Bryan is the second-oldest sibling in the Rosenau family :smile:"
		slack_client.api_call("chat.postMessage", channel=channel,
						  text=response1, as_user=True)
	if command.startswith(commandlist[3]):
		response1 = "Tom is the third-oldest sibling in the Rosenau family :smile:"
		slack_client.api_call("chat.postMessage", channel=channel,
						  text=response1, as_user=True)
	if command.startswith(commandlist[4]):
		response1 = "Nick is the youngest sibling in the Rosenau family :smile: (my master!)"
		slack_client.api_call("chat.postMessage", channel=channel,
						  text=response1, as_user=True)

	if command.startswith(commandlist[5]):
		response1 = "This is a surname of German and sometimes Ashkenasic medieval origins, of which it has several. As such it is either locational from a place called Rosenau, which means the place of the roses, or it may have been topoghraphical to describe a person who lived at a house with a sign of a rose, or occupational to describe a rose grower or perhaps a herbalist, one who used the rose for medicinal puposes, or it may have been from the female name Rose. In all cases the word, and hence the later surname is from the original Latin word 'rosa', intoduced into Germany before the 5th century A.D. There are no less than three coat of arms of the various Rosenau branches, of which the most popular is probably that of Westphalia being a canting of three silver roses on a black field."
		slack_client.api_call("chat.postMessage", channel=channel,
						  text=response1, as_user=True)

	if command.startswith(commandlist[6]):
		response1 = "'joke' = rosenbot tells a joke\n[zipcode] = enter your zipcode to get a link for weather and Yelp spots in your area\n'max,bryan,etc.' = get info on a brother\n'rosenau'=info on the Rosenau surname\n'who'= info about rosenbot\n'shutup'= tell rosenbot to shutup!\n'games'= see upcoming games from IGN\n'games switch'= see upcoming games for the Nintendo Switch\n'topt10'= list the top 10 nfl players in the 2017 season at this time\n'amazon'= list top selling items on Amazon at this time\n'netflix'= check if a movie is on netflix or not\n'notes' [text]= write a note\n'~notes'= look at all notes across sessions\n'#notes'= look at at all notes from this session\n'sms [-fromName] [/toName?] [message]' = send an SMS from slack using the format show here (the 'toName' must be setup beforehand to send the SMS to) "
		slack_client.api_call("chat.postMessage", channel=channel,
						  text=response1, as_user=True)

	if command.startswith(commandlist[7]):
		response1 = "I am rosenbot, a simple slackbot created using Python by Nick Rosenau on 10/15/2017"
		slack_client.api_call("chat.postMessage", channel=channel,
						  text=response1, as_user=True)
	
	
	if len(command) == 5 and command[0:5] not in commandlist and " " not in command:
		response2 = "Here's the weather for the zipcode: " + command + "\nhttps://weather.com/weather/today/l/" + command + ":4:US\n" + "Local resturants on Yelp:\n" + "https://www.yelp.com/search?find_desc=&find_loc=" + command + "&ns=1" 
		slack_client.api_call("chat.postMessage", channel=channel,
						  text=response2, as_user=True)
	if " " in command:
		ii = command.index(" ")
		if command[0:ii] not in commandlist:
			print command[0:ii]
			response2 = "Here's the weather for the zipcode: " + command + "\nhttps://weather.com/weather/today/l/" + command + ":4:US\n" + "Local resturants on Yelp:\n" + "https://www.yelp.com/search?find_desc=&find_loc=" + command + "&ns=1" 
			slack_client.api_call("chat.postMessage", channel=channel,
						  text=response2, as_user=True)
				

	if len(command) == 5 and '0' not in command and '1' not in command and '2' not in command and command not in commandlist and '+' not in command and '*' not in command and '-' not in command and '/' not in command:
		response = "Not sure what you mean. Use a *verified command* as listed through the 'help' command."
		slack_client.api_call("chat.postMessage", channel=channel,
						  text=response, as_user=True)

	if command.startswith(commandlist[8]):
		response1 = "Make me! :chloe: :chloe: :chloe:"
		slack_client.api_call("chat.postMessage", channel=channel,
						  text=response1, as_user=True)
	if command == commandlist[9]:
		response1 = "http://www.ign.com/upcoming/games"
		slack_client.api_call("chat.postMessage", channel=channel,
						  text=response1, as_user=True)
	if command == commandlist[10]:
		response1 = "http://www.ign.com/upcoming/games?platformSlug=nintendo-switch"
		slack_client.api_call("chat.postMessage", channel=channel,
						  text=response1, as_user=True)
	if command == commandlist[11]:
		txt = "OKAYYY"
		slack_client.api_call("chat.postMessage", channel=channel,
						  text=txt, as_user=True)	
		sresponse = playsound('/Users/nickrosenau/Desktop/Pythonproj/starterbot/okay.mp3')
		slack_client.api_call("chat.postMessage", channel=channel,
						  text=sresponse, as_user=True)	
	if command == commandlist[12]:
		el = str(newarray1)
		c = el.replace('[', "").replace("']", "").replace("u'", "").replace("'", "").replace("]", "").replace('"', "")
		response1 = "Top 10 NFL players and their points for the 2017 season:\n" + c
		slack_client.api_call("chat.postMessage", channel=channel,
						  text=response1, as_user=True)
	if command == commandlist[13]:
		el = str(new1)
		c = el.replace('[', "").replace("']", "").replace("u'", "").replace("'", "").replace("]", "").replace('"', "")
		response1 = "Some top-selling items in the Electronics department at Amazon:\n" + c
		slack_client.api_call("chat.postMessage", channel=channel,
						  text=response1, as_user=True)
	if command.startswith(commandlist[14]) and " " in command:
		netflixsearch = command[8:len(command)]
		url = "http://unogs.com/?q=" + netflixsearch + "-!1900,2017-!0,5-!0,10-!0,10-!Any-!Any-!Any-!Any-!I%20Don&cl=78&st=adv&ob=Relevance&p=1&ao=and"
		if " " in netflixsearch:
			funky = netflixsearch.replace(" ", "%20")
			url = "http://unogs.com/?q=" + funky + "-!1900,2017-!0,5-!0,10-!0,10-!Any-!Any-!Any-!Any-!I%20Don&cl=78&st=adv&ob=Relevance&p=1&ao=and"
		slack_client.api_call("chat.postMessage", channel=channel,
						  text=url, as_user=True)

	
	
	
	if command.startswith(commandlist[15]) and " " in command:
		notetxt = command[6:len(command)]
		
		if notetxt:
			#notepad.append(notetxt)
			
			blah = notetxt + ", "
			bby.append(blah)
			bah = notetxt + ", "
			text_file.write(bah)
			response1 = "Note stored."
			namesdb = open("names.txt", "r")
			testA = namesdb.read()
			testB = testA.replace(snaplen, "")
			
			x.append(testB)
			testD = snaplen.replace(testB, "")
			b=0
			i=0
			#print x
			
			
			if len(testA) - len(snaplen) >= 5:
			
				while i < len(x):
					fix = str(x[i]).replace("['", "").replace("']", "")
					testC = testA.replace(snaplen, "").replace(fix, "")
					i+=1
					print testC
					if testC != '':
						if len(testC) <= 5:
							test.append(testC)
						if len(testC) > 5:
							point = testC.index(',')
							pointy = testC[point:len(testC)]
							lol = testC.replace(pointy, "")
							test.append(lol)
					
			print test

				
			#j = testB.index(',')
			#zz = testB[0:j]
			#snaplen += zz
			
			#yoyo = len(testA) - len(snaplen)
			#pee = testA[len(testA)-yoyo:len(testA)]
			#pp = pee[]
			#test.append(testC)
			print snaplen
			print testA
			#print testB
			#print testC
			print len(testA) - len(snaplen)
			
			
			 
			
			slack_client.api_call("chat.postMessage", channel=channel,
						  text=response1, as_user=True)
			
			
			#test.append(testing)
	if command.startswith(commandlist[16]):
		c = thingy.replace('[', "").replace("']", "").replace("u'", "")
		#b = a.encode('ascii')
		response1 = "All notes:\n" + c
		
		slack_client.api_call("chat.postMessage", channel=channel,
						  text=response1, as_user=True)

	if command.startswith(commandlist[17]):
		#notetxt = command[6:len(command)]
		el = str(bby)
		c = el.replace("[u'", "").replace("']", "").replace("', u'", "")
		response1 = c
		slack_client.api_call("chat.postMessage", channel=channel,
						  text=response1, as_user=True)
	
	
	if command.startswith(commandlist[18]) and " " in command:
		if "-" in command:
			point = command.index('?')
			point0 = command.index('/')
			point1 = command.index('-')
			name = command[point0+1:point]
			from1 = command[point1+1:point0] 
			body1 = command[point+2:len(command)]
			body2 = "From " + from1 + "using rosenbot: " + "'"+ body1 + "'"

			if name == 'nick':
				client.messages.create(	to="+12035202065",
						from_="+16317598851",
						body=body2)

			response1 = 'Text sent.'
			slack_client.api_call("chat.postMessage", channel=channel,
						  text=response1, as_user=True)
			#for slack_message in sc.rtm_read():
				#usr = slack_message.get("user")
				#txt = slack_message.get('text')
				#txt1 = str(txt)
				#if usr == 'U7KF5HRNK' and 'sms' in txt1:
					#print 'Nick Rosenau'
	if command.startswith(commandlist[19]):
		i=0
		#print len(test)
		while i < len(bby) and i < len(test):
			newnotes = bby[i] + " " + test[i]
			slack_client.api_call("chat.postMessage", channel=channel,
						  text=newnotes, as_user=True)
			i+=1

	if command.startswith(commandlist[20]):
		snip = command[7:len(command)]
		rottenpage = requests.get("https://www.rottentomatoes.com/m/" + snip + "")
		if len(snip) - len(snip.replace(" ", "")) == 1:
			snip1 = snip.index(" ")
			snip0 = snip[0:snip1]
			cool = snip[snip1:len(snip)]
			cool1 = cool.replace(" ", "")
			rottenpage = requests.get("https://www.rottentomatoes.com/m/" + snip0 + "_" + cool1 + "")
		
			
		if len(snip) - len(snip.replace(" ", "")) == 2:
			snip1 = snip.index(" ")
			snip2 = snip.index(" ")
			snip0 = snip[0:snip1]
			b = snip.index(snip0)
			uh = snip[snip1:snip2]
			cool = snip[snip2:len(snip)]
			tryagain = cool[1:len(cool)]
			tryagain1 = tryagain.index(" ")
			try2 = tryagain[0:tryagain1]
			try3 = tryagain[tryagain1:len(tryagain)]
			cool1 = try2.replace(" ", "")
			cool2 = try3.replace(" ", "")
			rottenpage = requests.get("https://www.rottentomatoes.com/m/"+ snip0 + "_" + cool1 + "_" + cool2 + "")
		

		if len(snip) - len(snip.replace(" ", "")) == 3 and "the" in snip:
			print "ok"
			snip1 = snip.index(" ")
			snip2 = snip.index(" ")
			snip0 = snip[0:snip1]
			b = snip.index(snip0)
			uh = snip[snip1:snip2]
			cool = snip[snip2:len(snip)]
			tryagain = cool[1:len(cool)]
			tryagain1 = tryagain.index(" ")
			try2 = tryagain[0:tryagain1]
			try3 = tryagain[tryagain1:len(tryagain)]
			tryagain3 = try3[1:len(try3)]
			tryagain4 = tryagain3.index(" ")
			try4 = tryagain3[0:tryagain4]
			try5 = tryagain3[tryagain4:len(tryagain3)]
			print try4
			print try5
			cool1 = try2.replace(" ", "")
			#cool2 = try3.replace(" ", "")
			cool3 = try4.replace(" ", "")
			cool4 = try5.replace(" ", "")
			#link = "https://www.rottentomatoes.com/m/the_" + snip0 + "_" + cool1 + "_" + cool2 + "" 
			#index = link.index("m/")
			#link += "the_"
			rottenpage = requests.get("https://www.rottentomatoes.com/m/" + snip0 + "_" + cool1 + "_" + cool3 + "_" + cool4 + "")
			

		rtree = html.fromstring(rottenpage.content)
		score = rtree.xpath('//span[@class="meter-value superPageFontColor"]/span/text()')
		consensus = rtree.xpath('//*[contains(@class, "critic_consensus superPageFontColor")]//text()')

		

		z = ",".join(consensus[1:5])
		y = "".join(score[0:1])
		b = z.replace("   ", "")
		final = "Score: " + y + "%"+ " | " + b
		if ",Critics Consensus:" in final:
			a = final.replace(",Critics Consensus:", "")
			final = a
		if ".," in final:
			a = final.replace(".,", ".")
			final = a
		if ":," in final:
			a = final.replace(":,", ":")
			final = a
		if rottenpage:
			response1 = final
			slack_client.api_call("chat.postMessage", channel=channel,
						  text=response1, as_user=True)
		else:
			slack_client.api_call("chat.postMessage", channel=channel,
						  text="An error occured with the title of the movie you entered, try again.", as_user=True)
	if command.startswith(commandlist[21]):
		mathtxt = command[5:len(command)]
		if "sq" in mathtxt:
			i = mathtxt.index("sq")
			num = float(mathtxt[i+2:len(mathtxt)])
			response1 = math.sqrt(num)
			slack_client.api_call("chat.postMessage", channel=channel,
						  text=response1, as_user=True)
		if "cos" in mathtxt:
			i = mathtxt.index("cos")
			num = float(mathtxt[i+3:len(mathtxt)])
			response1 = math.cos(num)
			slack_client.api_call("chat.postMessage", channel=channel,
						  text=response1, as_user=True)
		if "sin" in mathtxt:
			i = mathtxt.index("sin")
			num = float(mathtxt[i+3:len(mathtxt)])
			response1 = math.sin(num)
			slack_client.api_call("chat.postMessage", channel=channel,
						  text=response1, as_user=True)
		if "tan" in mathtxt:
			i = mathtxt.index("tan")
			num = float(mathtxt[i+3:len(mathtxt)])
			response1 = math.tan(num)
			slack_client.api_call("chat.postMessage", channel=channel,
						  text=response1, as_user=True)
		if "deg" in mathtxt:
			i = mathtxt.index("deg")
			num = float(mathtxt[i+3:len(mathtxt)])
			response1 = math.degrees(num)
			slack_client.api_call("chat.postMessage", channel=channel,
						  text=response1, as_user=True)
		if "rad" in mathtxt:
			i = mathtxt.index("rad")
			num = float(mathtxt[i+3:len(mathtxt)])
			response1 = math.radians(num)
			slack_client.api_call("chat.postMessage", channel=channel,
						  text=response1, as_user=True)
		if "pow" in mathtxt:
			i = mathtxt.index("pow")
			comma = mathtxt.index(",")
			x = float(mathtxt[i+3:comma])
			y = float(mathtxt[comma+1:len(mathtxt)])
			response1 = math.pow(x,y)
			slack_client.api_call("chat.postMessage", channel=channel,
						  text=response1, as_user=True)
		if "%" in mathtxt:
			i = mathtxt.index("%")
			slash = mathtxt.index("/")
			x = float(mathtxt[i+1:slash])
			y = float(mathtxt[slash+1:len(mathtxt)])
			z = x/y
			txt = str(z*100)
			#response1 = txt + "%"
			#if len(txt) > 5:
			a = txt.replace(txt[5:len(txt)], "")
			response1 = a + "%"

			slack_client.api_call("chat.postMessage", channel=channel,
						  text=response1, as_user=True)
			

		#else:
			#slack_client.api_call("chat.postMessage", channel=channel,
						  #text="Mathematical operation not recognized.", as_user=True)



	if '+' in command:
		if len(command) == 3:
			response1 = int(command[0]) + int(command[2])
			slack_client.api_call("chat.postMessage", channel=channel,
						  text=response1, as_user=True)
		if len(command) == 5:
			response1 = int(command[0]+command[1]) + int(command[3]+command[4])
			slack_client.api_call("chat.postMessage", channel=channel,
						  text=response1, as_user=True)
		if len(command) == 7:
			response1 = int(command[0]+command[1]+command[2]) + int(command[4]+command[5]+command[6])
			slack_client.api_call("chat.postMessage", channel=channel,
						  text=response1, as_user=True)
	if '-' in command:
		if len(command) == 3:
			response1 = int(command[0]) - int(command[2])
			slack_client.api_call("chat.postMessage", channel=channel,
						  text=response1, as_user=True)
		if len(command) == 5:
			response1 = int(command[0]+command[1]) - int(command[3]+command[4])
			slack_client.api_call("chat.postMessage", channel=channel,
						  text=response1, as_user=True)
		if len(command) == 7:
			response1 = int(command[0]+command[1]+command[2]) - int(command[4]+command[5]+command[6])
			slack_client.api_call("chat.postMessage", channel=channel,
						  text=response1, as_user=True)
	if '*' in command:
		if len(command) == 3:
			response1 = int(command[0]) * int(command[2])
			slack_client.api_call("chat.postMessage", channel=channel,
						  text=response1, as_user=True)
		if len(command) == 5:
			response1 = int(command[0]+command[1]) * int(command[3]+command[4])
			slack_client.api_call("chat.postMessage", channel=channel,
						  text=response1, as_user=True)
		if len(command) == 6 and '.' not in command and command[2] == '*':
			response1 = int(command[0]+command[1]) * int(command[3]+command[4]+command[5])
			slack_client.api_call("chat.postMessage", channel=channel,
						  text=response1, as_user=True)
		if len(command) == 6 and '.' not in command and command[2] != '*':
			response1 = int(command[0]+command[1]+command[2]) * int(command[4]+command[5])
			slack_client.api_call("chat.postMessage", channel=channel,
						  text=response1, as_user=True)
		if len(command) == 6 and '.' in command:
			response1 = int(command[0]+command[1]) * float(command[4]+command[5])/100
			slack_client.api_call("chat.postMessage", channel=channel,
						  text=response1, as_user=True)
		if len(command) == 7:
			response1 = int(command[0]+command[1]+command[2]) * int(command[4]+command[5]+command[6])
			slack_client.api_call("chat.postMessage", channel=channel,
						  text=response1, as_user=True)

	if '/' in command:
		if len(command) == 3:
			response1 = float(command[0]) / float(command[2])
			slack_client.api_call("chat.postMessage", channel=channel,
						  text=response1, as_user=True)
		if len(command) == 5:
			response1 = float(command[0]+command[1]) / float(command[3]+command[4])
			slack_client.api_call("chat.postMessage", channel=channel,
						  text=response1, as_user=True)
		if len(command) == 6:
			response1 = float(command[0]+command[1]+command[2]) / float(command[4]+command[5])
			slack_client.api_call("chat.postMessage", channel=channel,
						  text=response1, as_user=True)
		if len(command) == 7:
			response1 = float(command[0]+command[1]+command[2]) / float(command[4]+command[5]+command[6])
			slack_client.api_call("chat.postMessage", channel=channel,
						  text=response1, as_user=True)
		if len(command) == 8 and command[5] != '/':
			response1 = float(command[0]+command[1]+command[2]+command[3]) / float(command[5]+command[6]+command[7])
			slack_client.api_call("chat.postMessage", channel=channel,
						  text=response1, as_user=True)
		if len(command) == 8 and command[5] == '/':
			response1 = float(command[0]+command[1]+command[2]+command[3]+command[4]) / float(command[6]+command[7])
			slack_client.api_call("chat.postMessage", channel=channel,
						  text=response1, as_user=True)


	

	#if einstein == True:
		#math1 = command
		#if command.startswith(math1):
			#zipp = False
			#mresponse = int(math1)*10
			#slack_client.api_call("chat.postMessage", channel=channel,
						  #text=mresponse, as_user=True)
	#if command != math1:
		#einstein = False
   
	
	#else:
		#response2 = "Hm...that doesn't look like a valid zipcode. Try again."
		#slack_client.api_call("chat.postMessage", channel=channel,
						  #text=response2, as_user=True)

def parse_slack_output(slack_rtm_output):
	"""
		The Slack Real Time Messaging API is an events firehose.
		this parsing function returns None unless a message is
		directed at the Bot, based on its ID.
	"""
	output_list = slack_rtm_output
	if output_list and len(output_list) > 0:
		for output in output_list:
			if output and 'text' in output and AT_BOT in output['text']:
				# return text after the @ mention, whitespace removed
				return output['text'].split(AT_BOT)[1].strip().lower(), \
					   output['channel']
	return None, None


if __name__ == "__main__":
		#c = user.get('id')
	#d = api_call.get('user')
	READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
	if slack_client.rtm_connect():
		print("rosenbot connected and running!")
		while True:
			command, channel = parse_slack_output(slack_client.rtm_read())
			if command and channel:
				handle_command(command, channel)
			time.sleep(READ_WEBSOCKET_DELAY)
	else:
		print("Connection failed. Invalid Slack token or bot ID?")