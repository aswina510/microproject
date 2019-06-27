# TWITTER ACCESING USING PYTHON
# AUTHORS ALBIN SUNNEY,ASWIN A


#CONTACT
# EMAIL: georgealways4u@gmail.com
#      : aswina007007@gmail.com
print "______________________________________________________________________________________________________________________________________________________"
print
print "                                                                   ASBIN TWITTER"
import json
import tweepy
CONSUMER_KEY = 'fC6fbrXMKPFhkDadBvzCBzKGz'
CONSUMER_SECRET = 'a2adoz9xrnEoUqtfVT7VTLKShaWG1JRU5p1X3n5T3JDDHDPNpi'
ACCESS_TOKEN = '793805525683232768-25qwPoExBWHEKpctpoFPUJvLPuEIlEs'
ACCESS_TOKEN_SECRET = 'IxyBovHHqedtModRPboaQ540pqBtgmASH4AGpe9NxQz0d'



#Authentication
auth =tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


while True:
	print"______________________________________________________________________________________________________________________________________________________"	
	print "1.New Tweet\n2.Show timeline\n3.search\n4.NO. OF FOLLOWERS\n5.My Tweets\nPRESS ANY OTHER KEY TO EXIT"
	ch=raw_input("Enter your choice :")
	print"\n\n"
#tweeting !
	if ch=='1':
		statu=raw_input("Enter your TWEEET :")
		api.update_status(status=statu)
		print "Your tweet was succesfully uploaded"

#timeline printer
	elif ch=='2':
		tweetsoftheday = api.home_timeline()		
		for tweet in tweetsoftheday:
			print"______________________________________________________________________________________________________________________________________________________"			
			print tweet.text
#making a search
	elif ch=='3':
		searchname=raw_input("Enter your search name :")		
		user = api.get_user(searchname)
		print "Screen Name:",user.screen_name
		print "Real name:",user.name
		print "Date of creation:",user.created_at
		print "No.of followers:"
		print user.followers_count
		print "People he follows:"
		for friend in user.friends():
	   		print "\tScreen name:",friend.screen_name
			print "\tReal name:",friend.name
#Followers count
	elif ch=='4':
		print "NO OF FOLLOWERZ"
		user = api.get_user("aswinashten")		
		print user.followers_count
#tweets published			
	elif ch=='5':	
		print "MY TWEETZ"		
		
		for tweet in tweepy.Cursor(api.user_timeline).items():
			dtweet=tweet._json
			print"______________________________________________________________________________________________________________________________________________________"			
			print "Tweet text:",dtweet["text"]
			print "Date of tweet:",dtweet["created_at"]
			print "Favorite counts:",dtweet["favorite_count"]
			print "Retweets:",dtweet["retweeted"]
			print "Language used:",dtweet["lang"] 

	
		 	
#Getting lost    			
	else:		
		print "######################################################################################################################################################"		
		r=raw_input("GET OUT!!(press enter)")
		print "######################################################################################################################################################"		
		break









#aswinashten
#aswinatwitter

