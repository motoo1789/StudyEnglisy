import json, config
from Tweete import tweete
from GetTimeline import getTimeline
#import tweepy
from requests_oauthlib import OAuth1Session

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET

twitter = OAuth1Session(CK,CS,AT,ATS)

tweete(twitter)