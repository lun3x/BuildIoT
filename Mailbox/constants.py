import tweepy
from secret_constants import *

# constants
mailboxHandle = 'youvegotmailbox'
whitelistUsers = ['ahmerb2', 'lun3x']

# set up API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
auth.set_access_token(access_token, access_secret_token)
api = tweepy.API(auth)
