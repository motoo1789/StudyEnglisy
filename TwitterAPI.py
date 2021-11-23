
import json, config
from Tweete import tweete
from GetTimeline import getTimeline
from ReadFile import readexe
from NLTK import nltkStart

#import tweepy
def main():
    # twitter = config.CreateOAuthSession()
    # getTimeline(twitter)
    dictFileInfo = readexe()
    nltkStart(dictFileInfo)

if __name__ == "__main__":
    main()