'''
Created on 16-Aug-2014

@author: Nishant Nawarkhede
@email : nishant.nawarkhede@gmail.com
'''
import tweepy
import urllib2
import json
consumer_key='##'
consumer_secret='##'
access_token_key='##'
access_token_secret='##'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)
api = tweepy.API(auth)

tweets_images=[]
tweets_videos=[]
tweets_text=[]
id_images=[]
id_videos=[]
public_tweets = api.user_timeline(screen_name="@yale",count=25,page=1,include_rts=False)
all_items=[]
[all_items.append(i) for i in public_tweets]

for i in all_items:
    try:
        if i.entities['media'][0]['type']=='photo':
            tweets_images.append({'url':i.entities['media'][0]['media_url'],'id':i.id})
            id_images.append(i.id)
    except:
        pass

for i in all_items:
    try:
        if i.id not in id_images:
            if i.entities['urls'][0]['expanded_url']:
                if 'youtube' in json.load(urllib2.urlopen('http://api.longurl.org/v2/expand?url='+i.entities['urls'][0]['expanded_url']+'&format=json'))['long-url']:
                    tweets_videos.append({'url':i.entities['urls'][0]['expanded_url'],'id':i.id}) 
                    id_videos.append(i.id)
    except Exception as e:
        pass

for i in all_items:
    if i.id not in id_images or i.id not in id_videos:
        tweets_text.append({'text':i.text,'id':i.id})

print tweets_text
print tweets_images
print tweets_videos