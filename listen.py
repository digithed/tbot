import os
import time
from slackclient import SlackClient
import vlc
import simplejson as json
from sklearn import tree

sc = SlackClient(os.environ.get('TATTLE_TOKEN'))
TATTLE_ID = os.environ.get("TATTLE_ID")
jobsquote = "_'Stay Hungry. Stay Foolish.' It was their farewell message as they signed off. Stay Hungry. Stay Foolish. And I have always wished that for myself. And now, as you graduate to begin anew, I wish that for you. Stay Hungry. Stay Foolish. - Steve Jobs, Stanford commencement speech_"
#music = json.toJSON(vlc.MediaPlayer("https://www.dropbox.com/s/m7vcfd62a9jb7im/OKAY.m4a?dl=0").__dict__)

noteNames = []
again = []
names_file = open("names.txt", "a")
array = []



if sc.rtm_connect():
		while True:
			for slack_messages in sc.rtm_read():
					txt = slack_messages.get('text')
					usr1 = slack_messages.get('user')
					if txt:
						yo = txt.encode('utf-8')
						usr = str(usr1)
						tt = str(slack_messages.get('type'))
						channels = slack_messages.get('channel')
						messages = [tt, yo, usr]
						i=0
						if messages[0] == 'message' and 'notes' in messages[1] and 'bryan' not in messages[1] and messages[2] == 'U7KF5HRNK':
							
							again.append("Nick,")
							print 'Nick'
							print again[i]
							print again

							while i < len(again):
								names_file = open("names.txt", "a")
								names_file.write(again[i])
								names_file.close()
								i+=1
						j=0
						if messages[0] == 'message' and 'notes' in messages[1] and 'bryan' in messages[1] and messages[2] == 'U7KF5HRNK':
							#names_file.write("Bryan,")
							again.append("Bryan,")
							print 'Bryan'
							print again[i]
							print again
							
							while j < len(again):
								names_file = open("names.txt", "a")
								names_file.write(again[i])
								names_file.close()
								j+=1
						if 'tattlebot' in yo and ('f' in yo or 'b' in yo):
							sc.api_call( "chat.postMessage", channel=channels, text="You got a problem? I will clean your clock.", as_user=True)
						if 'nobody cares' in yo and ('you' in yo or 'your' in yo or 'tattlebot' in yo):
							sc.api_call( "chat.postMessage", channel=channels, text="Oh yeah? Well I bet <@rosenbot> cares!", as_user=True)
						if 'sh' in yo and 'tattlebot' in yo:
							sc.api_call( "chat.postMessage", channel=channels, text="You are one nasty slack user!", as_user=True)
						if 'tattlebot' not in yo and ('f' in yo or 's' in yo or 'b' in yo):
							sc.api_call( "chat.postMessage", channel=channels, text="Oh! Such a naughty boy", as_user=True)
						if 'jobs' in yo:
							sc.api_call( "chat.postMessage", channel=channels, text=jobsquote, as_user=True)
						if 'tattlebot' == yo and usr == 'U7KFBEGCF':
							sc.api_call( "chat.postMessage", channel=channels, text="You want something from me, Bryan?", as_user=True)
						if 'tattlebot' == yo and usr == 'U7KF5HRNK':
							sc.api_call( "chat.postMessage", channel=channels, text="You want something from me, Nick?", as_user=True)
						if 'tattlebot' == yo and usr == 'U7KF4KBJB':
							sc.api_call( "chat.postMessage", channel=channels, text="You want something from me, Max?", as_user=True)
						if 'tattlebot' == yo and usr == 'U7HT7GQ01':
							sc.api_call( "chat.postMessage", channel=channels, text="You want something from me, Tom?", as_user=True)
						if 'who am i' in yo and usr == 'U7KFBEGCF':
							sc.api_call( "chat.postMessage", channel=channels, text="You're Bryan. You are 28 years old and live in Colorado.", as_user=True)
						if 'who am i' in yo and usr == 'U7KF5HRNK':
							sc.api_call( "chat.postMessage", channel=channels, text="You're Nick. You are 22 years old and live in Connecticut.", as_user=True)
						if 'who am i' in yo and usr == 'U7KF4KBJB':
							sc.api_call( "chat.postMessage", channel=channels, text="You're Max. You are 30 years old and live in Connecticut.", as_user=True)
						if 'who am i' in yo and usr == 'U7HT7GQ01':
							sc.api_call( "chat.postMessage", channel=channels, text="You're Tom. You are 24 years old and live in Colorado.", as_user=True)
						if 'ya little sheet' in yo:
							sc.api_call( "chat.postMessage", channel=channels, text="_Poohdawg was slapped._", as_user=True)
						if 'tattlebot' in yo and 'awesome' in yo or 'best' in yo or 'the man' in yo:
							sc.api_call( "chat.postMessage", channel=channels, text='Thank you...\n:sunglasses:', as_user=True)
						if '<@U7HSVHMLG> youtube' in yo:
							msg = yo
							msg1 = msg[13:len(msg)]
							array.append(msg1)
						if 'next' in yo:
							msg1 = array[0]
							if len(array) > 1:
								msg1 = array[-1]
							sc.api_call( "chat.postMessage", channel=channels, text='<@rosenbot> ' + msg1, as_user=True)
						bot = 0
						if 'kill' in yo:
							bot = 1

						ex = 0
						if 'life' in yo:
							ex += 50
						if 'myself' in yo:
							ex += 50
						if 'meaning' in yo:
							ex += 50
						if 'purpose' in yo:
							ex += 50
						# else:
						# 	ex +=10
						q = 0
						if 'what' in yo:
							q += 30
						if 'is' in yo:
							q += 30
						if 'the' in yo:
							q += 30
						if 'time' in yo:
							q += 30
						if 'how' in yo:
							q += 30
						if 'which' in yo:
							q += 30

						if 'tbot' in yo:
							index = yo.index('tbot')
							item = yo[0:index]
							if " " in item:
								
								rep = item.replace(" ", "%20")
								rep1 = rep.replace(' ', "")[:-3]
															

							url = 'https://www.google.com/search?q=' + rep1 + '&oq=' + rep1 + '&gs_l=psy-ab.3..0l2j0i131k1j0i67k1j0l2j0i46k1j46l2j0l3.18352.18936.0.19191.6.6.0.0.0.0.153.662.2j4.6.0....0...1.1.64.psy-ab..0.6.661...0i3k1.0.RRnRgqoLGBs'
							print ex
							print bot
							print q
							features = [[80,0,30], [5,0,0], [30,1,0], [5,0,80]]
							labels = ['life is what you make it', "I don't know. Go figure it out.", "don't do that!", 'I am not sure, but I googled it for you: '+ url]
							clf = tree.DecisionTreeClassifier()
							clf = clf.fit(features, labels)
							answer = clf.predict([[ex, bot, q]])
							test0 = str(answer)
							test = test0.replace("[", "").replace("]", "").replace("''", "").replace("''", "")
							test1 = test.replace("''", "")
						
							sc.api_call( "chat.postMessage", channel=channels, text=test1, as_user=True)
							
				
else:
		print "Connection Failed"