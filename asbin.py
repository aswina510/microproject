
print "______________________________________________________________________________________________________________________________________________________"
print
print "                                                                   ASBIN TWITTER"
import json
import tweepy
from tweepy.streaming import StreamListener
from tweepy import Stream
CONSUMER_KEY = 'fC6fbrXMKPFhkDadBvzCBzKGz'
CONSUMER_SECRET = 'a2adoz9xrnEoUqtfVT7VTLKShaWG1JRU5p1X3n5T3JDDHDPNpi'
ACCESS_TOKEN = '793805525683232768-25qwPoExBWHEKpctpoFPUJvLPuEIlEs'
ACCESS_TOKEN_SECRET = 'IxyBovHHqedtModRPboaQ540pqBtgmASH4AGpe9NxQz0d'



#Authentication
auth =tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
#
def process_or_store(tweet):
    print(json.dumps(tweet))

 
class MyListener(StreamListener):
 
    def on_data(self, data):
        #try:
            with open('python.json', 'a') as f:
                f.write(data)
                return True
        #except BaseException as e:
         #   print &quot,print Error on_data: %s&quot,print % str(e)
        #return True
 
    def on_error(self, status):
        print(status)
        return True
 

while True:
	print"______________________________________________________________________________________________________________________________________________________"	
	print "1.New Tweet\n2.Show timeline\n3.search\n4.FOLLOWING\n5.NO. OF FOLLOWERS\n6.My Tweets\nEXIT"
	ch=raw_input("Enter your choice Mahn :")
#tweeting mahn!
	if ch=='1':
		status=raw_input("Enter your TWEEET :")
		api.update_status(status=status)
		print "Your tweet was succesfully uploaded"

#timeline printer
	elif ch=='2':
		public_tweets = api.home_timeline()
		for tweet in public_tweets:
			print tweet.text
	elif ch=='3':
		friend=raw_input("Enter your search name :")		
		user = api.get_user(friend)
		print user.screen_name
		print "No.of followers:"
		print user.followers_count
		print "People he follows:"
		for friend in user.friends():
	   		print friend.screen_name
	elif ch=='4':
		print "FOLLOWERING"		
		for friend in tweepy.Cursor(api.friends).items():
    			process_or_store(friend._json)
	elif ch=='6':	
		print "MY TWEETZ"
		for tweet in tweepy.Cursor(api.user_timeline).items():
    			process_or_store(tweet._json)
	elif ch=='5':
		print "NO OF FOLLOWERZ"
		user = api.get_user("aswinashten")		
		print user.followers_count
		 	
	elif ch=='7':
		twitter_stream = Stream(auth, MyListener())
		twitter_stream.filter(track=['Testing'])
#Getting lost    			
	else:		
		print "######################################################################################################################################################"		
		r=raw_input("GET OUT!!(press enter)")
		print "######################################################################################################################################################"		
		break









#aswinashten
#aswinatwitter

