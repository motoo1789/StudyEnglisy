import json, config
from Tweete import tweete
from GetTimeline import getTimeline
#import tweepy
def main():
    twitter = config.CreateOAuthSession()
    getTimeline(twitter)

if __name__ == "__main__":
    main()