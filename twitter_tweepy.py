# Twitter API

# Install:
# pip install tweepy

# Make a new application to get access keys and secrets.
# https://apps.twitter.com/app/new
# You can change permissions from read only to allow read/write at the permisions tab but this will require you 
# to ask for a new access token at the "Keys and Access Tokens" tab.

# Structure of Json-Data:
# https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/tweet-object
# https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/user-object


from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json

# consumer key, consumer secret, access token, access secret.
ckey="asdfsafsafsaf"
csecret="asdfasdfsadfsa"
atoken="asdfsadfsafsaf-asdfsaf"
asecret="asdfsadfsadfsadfsadfsad"

from twitterapistuff import *

class listener(StreamListener):

    def on_data(self, data):

		all_data = json.loads(data)							# json module to load the data var 

		tweet =  ascii(all_data["text"])

    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["happy"])
