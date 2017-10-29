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
import random
from datetime import datetime
import PySide
import numpy



page = requests.get("http://www.nfl.com/scores/2017")

tree = html.fromstring(page.content)

team = tree.xpath('//p[@class="team-name"]/a/text()')

scores = tree.xpath('//p[@class="total-score"]/text()')

date = tree.xpath('//span[@title="Date Airing"]/text()')

channel = tree.xpath('//span[@title="Airing on Network Channel"]/text()')

gametime = tree.xpath('//span[@class="time-left"]/text()')
ccc = []
	

test9 = datetime.now().strftime('%H:%M')
test99 = int(test9[0:2]) - 12
test8 = datetime.now().strftime('%d')
test88 = test8

currentTime = str(test99) + datetime.now().strftime('%M')

# Function for pulling live nfl scores while still using lxml
i=0
j=0
abcd = []
while j < len(team) or j < len(scores) or i < len(date) or i < len(gametime) or i < len(channel):
	if j == 29:
		break

	url = requests.get("http://www.nfl.com/scores/2017")
	string = str(url.text)
	index0 = string.index('"identifier":'+'"'+team[j]+'"')
	index1 = string.index('"identifier":'+'"'+team[j+1]+'"')
	#index = string.index('"points":')
	dope = string[index0:index0+60]
	dope1 = string[index1:index1+60]
	dopeind0 = dope.find('"points":')
	dopeind = dope1.find('"points":')
	aaa = dope[dopeind0+9:dopeind0+11]
	bbb = dope1[dopeind+9:dopeind+11]

	
	if ' #{clock}' in gametime:
		b = team[j] + " " + "(" + bbb + ")" + " vs. " + team[j+1] + " " +  "(" + aaa + ")" + gametime[i]
		if ' #{clock}' in b:
			print 'true'
			url = requests.get("http://www.nfl.com/scores/2017")
			string = str(url.text)
			index0 = string.index('"identifier":'+'"'+team[j]+'"')
			index1 = string.index('"identifier":'+'"'+team[j+1]+'"')
			#index = string.index('"points":')
			dope = string[index0:index0+60]
			dope1 = string[index1:index1+60]
			dopeind0 = dope.index('"points":')
			dopeind = dope1.index('"points":')
			aaa = dope[dopeind0+9:dopeind0+11]
			bbb = dope1[dopeind+9:dopeind+11]
			if "," in aaa or "," in bbb:
				aaa = dope[dopeind0+9:dopeind0+11].replace(",", "")
				bbb = dope1[dopeind+9:dopeind+11].replace(",", "")
			b = team[j] + " " + "(" + aaa + ")" + " vs. " + team[j+1] + " " +  "(" + bbb + ")" +  " | " + 'Game Active!' + " | " + channel[i]
			abcd.append(b)

		if i <=11:
			b = team[j] + " " + "(" + scores[j] + ")" + " vs. " + team[j+1] + " " +  "(" + scores[j+1] + ")" + " | " + channel[i] + " | " + gametime[i]
			if '#{away.score.T}' not in b:
				abcd.append(b)
	
	if i <=11:
		b = team[j] + " " + "(" + scores[j] + ")" + " vs. " + team[j+1] + " " +  "(" + scores[j+1] + ")" + " | " + date[i] + " | " + channel[i] + " | " + gametime[i] 
		abcd.append(b)
		if i==12:
			break
	if 'FINAL' in gametime[i]:
		b1 = team[j] + " " + "(" + scores[j] + ")" + " vs. " + team[j+1] + " " +  "(" + scores[j+1] + ")" + " | " + gametime[i]
		abcd.append(b1)
			
	j+=2
	i+=1
	

#resources for pulling top 10 nfl player stats
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

#resources for pulling top items on Amazon
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

#resources for "Notes" function
text_file = open("notes.txt", "a")
test = []
x = []

#Bot ID, Slack ID, and command list
BOT_ID = os.environ.get("BOT_ID")
AT_BOT = "<@" + BOT_ID + ">"
commandlist = ["joke","m","b","t","nick","xyz","help","who","shut it!","games","games switch","ok","top10","amazon","netflix","notes","~notes","#notes","sms","test","rotten","math","youtube","cares","nfl"]

slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))

sc = slack_client
bby = []
read = []
snapshot = open("names.txt", "r")
snaplen = snapshot.read()
b=0

#The following function eceives commands directed at the bot and determines their validity
def handle_command(command, channel):
	
	l = []
	for i in commandlist:
		if i not in command:
			l.append(1)
		else:
			l.append(0)		
	
	if 0 not in l:
		response = "Not sure what you mean. Use a *verified command* as listed through the 'help' command."
		slack_client.api_call("chat.postMessage", channel=channel,
						  text=response, as_user=True)

	if command.startswith(commandlist[0]):
		response = "Knock! Knock! Who's there? Banana. Banana who? But Nana said my name was Nick."
		slack_client.api_call("chat.postMessage", channel=channel,
						  text=response, as_user=True)
	if command.startswith(commandlist[1]):
		response1 = "m is the oldest sibling in the xyz family :smile:"
		slack_client.api_call("chat.postMessage", channel=channel,
						  text=response1, as_user=True)
	if command.startswith(commandlist[2]):
		response1 = "b is the second-oldest sibling in the xyz family :smile:"
		slack_client.api_call("chat.postMessage", channel=channel,
						  text=response1, as_user=True)
	if command.startswith(commandlist[3]):
		response1 = "t is the third-oldest sibling in the xyz family :smile:"
		slack_client.api_call("chat.postMessage", channel=channel,
						  text=response1, as_user=True)
	if command.startswith(commandlist[4]):
		response1 = "Nick is the youngest sibling in the xyz family :smile: (my master!)"
		slack_client.api_call("chat.postMessage", channel=channel,
						  text=response1, as_user=True)

	if command.startswith(commandlist[5]):
		response1 = "This is a name of German and sometimes Ashkenasic medieval origins, of which it has several. As such it is either locational from a place called xyz, which means the place of the roses, or it may have been topoghraphical to describe a person who lived at a house with a sign of a rose, or occupational to describe a rose grower or perhaps a herbalist, one who used the rose for medicinal puposes, or it may have been from the female name Rose. In all cases the word, and hence the later surname is from the original Latin word 'rosa', intoduced into Germany before the 5th century A.D. There are no less than three coat of arms of the various xyz branches, of which the most popular is probably that of Westphalia being a canting of three silver roses on a black field."
		slack_client.api_call("chat.postMessage", channel=channel,
						  text=response1, as_user=True)

	if command.startswith(commandlist[6]):
		response1 = "'joke' = rosenbot tells a joke\n[zipcode] = enter your zipcode to get a link for weather and Yelp spots in your area\n'm,b,etc.' = get info on a brother\n'xyz'=info on the xyz surname\n'who'= info about rosenbot\n'shutup'= tell rosenbot to shutup!\n'games'= see upcoming games from IGN\n'games switch'= see upcoming games for the Nintendo Switch\n'topt10'= list the top 10 nfl players in the 2017 season at this time\n'amazon'= list top selling items on Amazon at this time\n'netflix'= check if a movie is on netflix or not\n'notes' [text]= write a note\n'~notes'= look at all notes across sessions\n'#notes'= look at at all notes from this session\n'sms [-fromName] [/toName?] [message]' = send an SMS from slack using the format show here (the 'toName' must be setup beforehand to send the SMS to) "
		slack_client.api_call("chat.postMessage", channel=channel,
						  text=response1, as_user=True)

	if command.startswith(commandlist[7]):
		response1 = "I am rosenbot, a simple slackbot created using Python by Nick xyz on 10/15/2017"
		slack_client.api_call("chat.postMessage", channel=channel,
						  text=response1, as_user=True)
	
#Weather and yelp info based on zipcode entered through Slack message
	if len(command) == 5 and command[0:5] not in commandlist and " " not in command:
		response2 = "Here's the weather for the zipcode: " + command + "\nhttps://weather.com/weather/today/l/" + command + ":4:US\n" + "Local resturants on Yelp:\n" + "https://www.yelp.com/search?find_desc=&find_loc=" + command + "&ns=1" 
		slack_client.api_call("chat.postMessage", channel=channel,
						  text=response2, as_user=True)			

	if len(command) == 5 and '0' not in command and '1' not in command and '2' not in command and command not in commandlist and '+' not in command and '*' not in command and '-' not in command and '/' not in command:
		response = "Not sure what you mean. Use a *verified command* as listed through the 'help' command."
		slack_client.api_call("chat.postMessage", channel=channel,
						  text=response, as_user=True)

	if command.startswith(commandlist[8]):
		response1 = "Make me! :smile:"
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
		sresponse = playsound('/nickxyz/Desktop/okay.mp3')
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
			blah = notetxt + ", " + datetime.now().strftime('%m:%d:%H:%M')
			bby.append(blah)
			bah = notetxt + ", "
			text_file.write(bah)
			response1 = "Note stored."
	
			slack_client.api_call("chat.postMessage", channel=channel,
						  text=response1, as_user=True)
			
			
	if command.startswith(commandlist[16]):
		c = thingy.replace('[', "").replace("']", "").replace("u'", "")
		response1 = "All notes:\n" + c
		
		slack_client.api_call("chat.postMessage", channel=channel,
						  text=response1, as_user=True)

	if command.startswith(commandlist[17]):
		el = str(bby)
		c = el.replace("[u'", "").replace("']", "").replace("', u'", "")
		response1 = c
		slack_client.api_call("chat.postMessage", channel=channel,
						  text=response1, as_user=True)
	
#function for sending sms through Slack messages
	if command.startswith(commandlist[18]) and " " in command:
		if "-" in command:
			point = command.index('?')
			point0 = command.index('/')
			point1 = command.index('-')
			name = command[point0+1:point]
			from1 = command[point1+1:point0] 
			body1 = command[point+2:len(command)]
			body2 = "From " + from1 + "using rosenbot: " + "'"+ body1 + "'"

			if name == 'Joe':
				client.messages.create(	to="0",
						from_="0",
						body=body2)

			response1 = 'Text sent.'
			slack_client.api_call("chat.postMessage", channel=channel,
						  text=response1, as_user=True)
			for slack_message in sc.rtm_read():
				usr = slack_message.get("user")
				txt = slack_message.get('text')
				txt1 = str(txt)
				if usr == 'xyz' and 'sms' in txt1:
					print 'Joe'
	if command.startswith(commandlist[19]):
		i=0
		while i < len(bby) and i < len(test):
			newnotes = bby[i] + " " + test[i]
			slack_client.api_call("chat.postMessage", channel=channel,
						  text=newnotes, as_user=True)
			i+=1

#extensive code below for rottentatoes.com "rotten score" lookup
	if command.startswith(commandlist[20]):
		snip = command[7:len(command)]
		if 'rottentv' in command[0:8]:
			snip = command[9:len(command)]
		rottenpage = requests.get("https://www.rottentatoes.com/m/" + snip + "")
		if 'rottentv' in command[0:8] and len(snip) - len(snip.replace(" ", "")) == 0:
			print 'yes'
			rottenpage = requests.get("https://www.rottentatoes.com/tv/" + snip + "")
		if len(snip) - len(snip.replace(" ", "")) == 1:
			snip1 = snip.index(" ")
			snip0 = snip[0:snip1]
			cool = snip[snip1:len(snip)]
			cool1 = cool.replace(" ", "")
			rottenpage = requests.get("https://www.rottentatoes.com/m/" + snip0 + "_" + cool1 + "")
			if 'rottentv' in command[0:8]:
				print 'no'
				rottenpage = requests.get("https://www.rottentatoes.com/tv/" + snip0 + "_" + cool1 + "")
		
			
		if len(snip) - len(snip.replace(" ", "")) == 2:
			snip1 = snip.index(" ")
			snip2 = snip.index(" ")
			snip0 = snip[0:snip1]
			b = snip.index(snip0)
			u = snip[snip1:snip2]
			cool = snip[snip2:len(snip)]
			tryagain = cool[1:len(cool)]
			tryagain1 = tryagain.index(" ")
			try2 = tryagain[0:tryagain1]
			try3 = tryagain[tryagain1:len(tryagain)]
			cool1 = try2.replace(" ", "")
			cool2 = try3.replace(" ", "")
			rottenpage = requests.get("https://www.rottentatoes.com/m/"+ snip0 + "_" + cool1 + "_" + cool2 + "")
			if 'rottentv' in command[0:8]:
				print 'its here'
				print "https://www.rottentatoes.com/tv/"+ snip0 + "_" + cool1 + "_" + cool2 + ""
				rottenpage = requests.get("https://www.rottentatoes.com/tv/" + snip0 + "_" + cool1 + "_" + cool2 + "")
		

		if len(snip) - len(snip.replace(" ", "")) == 3 and "the" in snip:
			
			snip1 = snip.index(" ")
			snip2 = snip.index(" ")
			snip0 = snip[0:snip1]
			b = snip.index(snip0)
			u = snip[snip1:snip2]
			cool = snip[snip2:len(snip)]
			tryagain = cool[1:len(cool)]
			tryagain1 = tryagain.index(" ")
			try2 = tryagain[0:tryagain1]
			try3 = tryagain[tryagain1:len(tryagain)]
			tryagain3 = try3[1:len(try3)]
			tryagain4 = tryagain3.index(" ")
			try4 = tryagain3[0:tryagain4]
			try5 = tryagain3[tryagain4:len(tryagain3)]
		
			cool1 = try2.replace(" ", "")
			cool3 = try4.replace(" ", "")
			cool4 = try5.replace(" ", "")
			rottenpage = requests.get("https://www.rottentatoes.com/m/" + snip0 + "_" + cool1 + "_" + cool3 + "_" + cool4 + "")
			if 'rottentv' in command[0:8]:
				rottenpage = requests.get("https://www.rottentatoes.com/tv/" + snip0 + "_" + cool1 + "_" + cool3 + "_" + cool4 + "")
			
		if 'rottentv' in command:
			rtree = html.fromstring(rottenpage.content)
			score = rtree.xpath('//span[@class="meter-value superPageFontColor"]/span/text()')
			consensus = rtree.xpath('//div[@class="movie_synopsis clamp clamp-6 clearfix"]//text()')
			if not rottenpage:
				slack_client.api_call("chat.postMessage", channel=channel,
						  text="An error occured with the title of the tv show you entered, try again.", as_user=True)
			if rottenpage:
				z = consensus[0]
				y = "".join(score[0:1])
				b = z.replace("   ", "")
				final = "Score: " + y + "%"+ " | " + "Critics Consensus: " + b
				response1 = final
				slack_client.api_call("chat.postMessage", channel=channel,
							  text=response1, as_user=True)
		if 'rottentv' not in command:	
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
			if rottenpage and 'rottentv' not in command:
				response1 = final
				slack_client.api_call("chat.postMessage", channel=channel,
							  text=response1, as_user=True)
			else:
				slack_client.api_call("chat.postMessage", channel=channel,
							  text="An error occured with the title of the movie you entered, try again.", as_user=True)

#scientific calculator function
	if command.startswith(commandlist[21]):
		mathtxt = command[5:len(command)]
		if "+" in mathtxt:
			i = mathtxt.index("+")
			num = float(mathtxt[0:i])
			num1 = float(mathtxt[i:len(mathtxt)])
			response1 = int(num+num1)
			slack_client.api_call("chat.postMessage", channel=channel,
						  text=response1, as_user=True)
		if "-" in mathtxt:
			i = mathtxt.index("-")
			num = float(mathtxt[0:i])
			num1 = float(mathtxt[i+1:len(mathtxt)])
			print num
			print num1
			response1 = int(num - num1)
			slack_client.api_call("chat.postMessage", channel=channel,
						  text=response1, as_user=True)
		if "*" in mathtxt:
			i = mathtxt.index("*")
			num = float(mathtxt[0:i])
			num1 = float(mathtxt[i+1:len(mathtxt)])
			response1 = int(num*num1)
			slack_client.api_call("chat.postMessage", channel=channel,
						  text=response1, as_user=True)
		if "/" in mathtxt and "%" not in mathtxt:
			i = mathtxt.index("/")
			num = float(mathtxt[0:i])
			num1 = float(mathtxt[i+1:len(mathtxt)])
			response1 = float(num/num1)
			slack_client.api_call("chat.postMessage", channel=channel,
						  text=response1, as_user=True)
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
		if "%" in mathtxt and "/" in mathtxt:
			i = mathtxt.index("%")
			slash = mathtxt.index("/")
			x = float(mathtxt[i+1:slash])
			y = float(mathtxt[slash+1:len(mathtxt)])
			z = x/y
			txt = str(z*100)
			a = txt.replace(txt[5:len(txt)], "")
			response1 = a + "%"
			slack_client.api_call("chat.postMessage", channel=channel,
						  text=response1, as_user=True)
		if "%" in mathtxt and "of" in mathtxt:
			i = mathtxt.index("%")
			slash = mathtxt.index("of")
			x = float(mathtxt[i+1:slash])
			y = float(mathtxt[slash+2:len(mathtxt)])
			z = x/100
			txt = str(z*y)
			slack_client.api_call("chat.postMessage", channel=channel,
						  text=txt, as_user=True)
		eqlist = ['+','-','/','*','%','of','pow','sq','cos','sin','tan','deg','rad']
		list0 = []
		for i in eqlist:
			if i in command:
				list0.append(0)
		if 0 not in list0:
			slack_client.api_call("chat.postMessage", channel=channel,
						  text='Unrecognized equation. Please try again.', as_user=True)
#youtube randomizer
	if command.startswith(commandlist[22]):
		v = command[8:len(command)]
		page = requests.get("https://www.youtube.com/results?search_query=" + v)
		tree = html.fromstring(page.content)
		find = tree.xpath('//a/@href')
		x = []
		for i in find:
			if '/watch?v' in i and 'gaming.youtube' not in i:
				x.append(i)

		def myfunc():
			z = random.choice(x)
			page1 = requests.get("https://www.youtube.com" + z)
			
			tree1 = html.fromstring(page1.content)

			newviews = tree1.xpath('//div[@class="watch-view-count"]/text()')

			for i in newviews:
				index = i.index(" ")

				change = i[0:index]
				
				change1 = change.replace(",", "")
				results = [int(change1)]

		#filter video results by number of views
				for j in results:
					if j > 50000:
						response1 = "https://www.youtube.com" + z
						slack_client.api_call("chat.postMessage", channel=channel,
					  	text=response1, as_user=True)
					if j < 50000:
						z = random.choice(x)
						myfunc()

		myfunc()

		
			
	if command.startswith(commandlist[23]):
		slack_client.api_call("chat.postMessage", channel=channel,
						  text="tattlebot is right, I do care :heart:", as_user=True)
			
	if command.startswith(commandlist[24]):
		for i in abcd:
			slack_client.api_call("chat.postMessage", channel=channel,
						  text=i, as_user=True)
		

def parse_slack_output(slack_rtm_output):
	output_list = slack_rtm_output
	if output_list and len(output_list) > 0:
		for output in output_list:
			if output and 'text' in output and AT_BOT in output['text']:
				# return text after the @ mention, whitespace removed
				return output['text'].split(AT_BOT)[1].strip().lower(), \
					   output['channel']
	return None, None


if __name__ == "__main__":
	READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading
	if slack_client.rtm_connect():
		print("rosenbot connected and running!")
		while True:
			command, channel = parse_slack_output(slack_client.rtm_read())
			if command and channel:
				handle_command(command, channel)
			time.sleep(READ_WEBSOCKET_DELAY)
	else:
		print("Connection failed. Invalid Slack token or bot ID?")