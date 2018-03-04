
# Unit 7 Assignment - Distinguishing Sentiments -CHU
Observable Trend 1: New York Times has the highest compound range based on tweets on 3/4
Observable Trend 2: Tweets mentioning New York Times skew negative, especially in comparison to BBC, CBS, CNN, and Fox News
Observable Trend 3: Tweets mentioning BBC News skews more positive, especially in comparison to CBS, CNN, Fox News, and NY Times


```python
import tweepy
import json
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
from localenv import consumer_key, consumer_secret, access_token, access_token_secret
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()
import seaborn as sns
import os
import csv
from localenv import (consumer_key, 
                    consumer_secret, 
                    access_token, 
                    access_token_secret)
```


```python
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
```


```python
target_terms = ("@BBCWorld", "@CBS", "@CNN", "@FoxNews", "@nytimes")
counter=1
sentiment=[]
for target in target_terms:
    oldest_tweet = None
    compound=[]
    pos=[]
    neg=[]
    neu=[]

    for x in range(2):
        public_tweets=api.search(target, count=100, result_type="recent", max_id=oldest_tweet)
        for tweet in public_tweets["statuses"]:
            results=analyzer.polarity_scores(tweet["text"])
            compound=results["compound"]
            pos=results["pos"]
            neu=results["neu"]
            neg=results["neg"]
              
            sentiment.append({"User":target,
               "Compound": compound,
               "Positive": pos,
               "Negative": neg,
               "Neutral": neu,
               "Tweet Count": counter})
            counter = counter + 1
    oldest_tweet=int(tweet['id_str'])-1
```


```python
sentiments_pd=pd.DataFrame.from_dict(sentiment)
sentiments_pd.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Compound</th>
      <th>Negative</th>
      <th>Neutral</th>
      <th>Positive</th>
      <th>Tweet Count</th>
      <th>User</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.4215</td>
      <td>0.000</td>
      <td>0.882</td>
      <td>0.118</td>
      <td>1</td>
      <td>@BBCWorld</td>
    </tr>
    <tr>
      <th>1</th>
      <td>-0.1027</td>
      <td>0.097</td>
      <td>0.903</td>
      <td>0.000</td>
      <td>2</td>
      <td>@BBCWorld</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.4215</td>
      <td>0.000</td>
      <td>0.882</td>
      <td>0.118</td>
      <td>3</td>
      <td>@BBCWorld</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.0000</td>
      <td>0.000</td>
      <td>1.000</td>
      <td>0.000</td>
      <td>4</td>
      <td>@BBCWorld</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.2714</td>
      <td>0.353</td>
      <td>0.141</td>
      <td>0.506</td>
      <td>5</td>
      <td>@BBCWorld</td>
    </tr>
  </tbody>
</table>
</div>




```python
sentiments_pd.to_csv("07TweetCSV_Chu.csv", index=False)
```


```python
plt.plot(np.arange(len(sentiments_pd["Compound"])),sentiments_pd["Compound"], marker="o", linewidth=0.5, alpha=0.8)
now = datetime.now()
now = now.strftime("%Y-%m-%d %H:%M")
plt.title("Sentiment Analysis of Tweets ({}) for {}".format(now, target))
plt.ylabel("Tweet Polarity")
plt.xlabel("Tweets Ago")
plt.show()
```


![png](output_6_0.png)



```python
sns.lmplot(x="Tweet Count", 
           y="Compound",
           data=sentiments_pd,
           fit_reg=False, 
           palette="viridis",
           hue="User",
           legend=True)
now = datetime.now()
now = now.strftime("%Y-%m-%d %H:%M")
plt.title("Sentiment Analysis of Media Tweets ({})".format(now))
plt.ylabel("Tweet Polarity")
plt.xlabel("Tweets Ago")
plt.savefig("SentimentAnalysis1_Chu")
```


![png](output_7_0.png)



```python
sns.barplot(x="User",
           y= "Compound",
           data = sentiments_pd,
            palette="viridis",
           order=None,
           hue_order="User")
now = datetime.now()
now = now.strftime("%Y-%m-%d %H:%M")
plt.title("Overall Media Sentiment based on Twitter({})".format(now))
plt.savefig("SentimentAnalysis2_Chu")
```


![png](output_8_0.png)

