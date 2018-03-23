# General:
import tweepy           # To consume Twitter's API
import pandas as pd    # To handle data
import numpy as np      # For number computing
from textblob import TextBlob
import re
import csv

# For plotting and visualization:
##%matlotlib inline
##from IPython.display import display
##import matplotlib.animation as animation
##import matplotlib.pyplot as plt
##%matlotlib inline
##import seaborn as sns

##plt.style.use('ggplot')
##fig=plt.figure()
##ax1=fig.add_subplot(1,1,1)
##ax2=fig.add_subplot(1,1,1)
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''


# API's setup:
def twitter_setup():
    """
    Utility function to setup the Twitter's API
    with our access keys provided.
    """
    # Authentication and access using keys:
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Return API with authentication:
    api = tweepy.API(auth)
    return api

extractor = twitter_setup()
data=extractor.trends_place(1)
data1=[]
##d=pd.DataFrame(data)
##print(data)
##def getValueOf(k, data):
##    for d in data:
##        for l in d:
##            if k in l:
##                return l[k]
##
##a=[]
##a=getValueOf('name',data)
##print(a)
for location in data:
	for trend in location["trends"]:
		print (" - %s" % trend["name"])
		data1.append(trend["name"])
		
print(data1)
df=pd.DataFrame(data1)
print(df.head(10))
##data2=data1.encode("utf-8")
##with open('trends_tweets.csv', 'wb') as f: 
##    writer = csv.writer(f)
##    writer.writerows(data1)
##pass 
df.to_csv("sss.csv",index=False,header=False)




