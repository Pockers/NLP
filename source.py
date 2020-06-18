import json
import tweepy
import re
import csv


aKey= tweepy.OAuthHandler(consKey, consKeySec)
aKey.set_access_token(acToken, acTokenSec)

api=tweepy.API(aKey)

hashtag= input('Please enter the hashtag\n')

for tweet in tweepy.Cursor(api.search,q=hashtag+' -filter:retweets', lang="en", tweet_mode='extended').items(1000) : 
    print(tweet.full_text.replace('\n', ' '))
    print('\n')
