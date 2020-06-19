import json
import tweepy
import re
import csv
from textblob import TextBlob
import re


consKey='m7D3STDCc6WMuZdIXDejSyZxi'
consKeySec='suKdHr0ORtIYbqRxH3H1x6aNHcwxVlsgnBmtUbWjOEkxzPlyXV'
acToken='1272604412666621957-oOVZTyJNKT0iGhSz04ptn6kKeA9i4F'
acTokenSec='ELMqJ0M9RGYdb3AtvwI806beAisEuJHrh50VPk1IgaLQS'


aKey= tweepy.OAuthHandler(consKey, consKeySec)
aKey.set_access_token(acToken, acTokenSec)

api=tweepy.API(aKey)

hashtag= input('Please enter the hashtag\n')
hashtagList=hashtag.split()
avg=0
maxTweets=1000
sentScore=0


for x in hashtagList:
    for tweet in tweepy.Cursor(api.search,q=x+' -filter:retweets', lang="en", tweet_mode='extended').items(maxTweets) : 
        tweetSent=TextBlob(tweet.full_text)
        sentScore+=tweetSent.sentiment.polarity
        print(tweet.full_text.replace('\n', ' '))
        print('\n')

avg=sentScore/maxTweets
print("The sentiment score for "+str(maxTweets)+" is "+str(round(avg*100,2)))
 
