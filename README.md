# python-twitter-text-image-video

**Separating tweets from text, image , videos using Tweepy – Python**

The twitter api doesn’t provide any mechanism that distinguish the tweets from text , image and videos. If we want to separate it then we have to do it manually. I was searching on internet , but I couldn’t find any simple solution for this.
So here is what I have tried. If you are beginner then it is good for you. And if you are experienced then please reply me for another solution for this. You can easily find out the tweet is image or not. Tweet object contains type property.


```
<tweet-object>.entities[‘media’][0][‘type’]==’photo’ 
```

If <code> i.entities[‘media’][0][‘type’]==’photo’ </code>  then you can guess it is image.

But <code> <tweet-object>.entities[‘media’][0][‘type’] </code> is only present in case of Images.

Now its time for video’s. Extract all the url’s from the <code>  <tweet-object>.entities[‘urls’][0][‘expanded_url’] </code>  . It returns the shorten url . You have to find out original url for this shorten url. There are many api available to do this.

Next is filter the urls from keywords. You can easily judge url for videos,

e.g if url contains keyword like youtube or vimeo then it is probabaly video url.
