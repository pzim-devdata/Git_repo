#!/usr/bin/env python
# coding: utf-8

# In[2]:


#pip install tweepy')
#import twitter
import tweepy

#### On remplace ici les valeurs des Key, secret et Token par celle de l'application crée sur l'environnement twitter
CONSUMER_KEY = 'ZJyhgelWsFYnRKDPyGEXaCwkk'
CONSUMER_SECRET = 'dcohnsZaqPV9zlqz3aFjQmOXeKCaFNMOfmZ6fSbuuyPiwSkNO3'
OAUTH_TOKEN = '1146751549282148352-WVM8z9n77P4zhl7F11RJuTdeG5r6go'
OAUTH_TOKEN_SECRET = 'TQGtNYyD3FBSXXdVkL7bLKhwNcHuUNsIwVezDSEWPuTaq'

##### Connecxion à l'API
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
#  Token and secret
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

# Création de l'API
api = tweepy.API(auth) 

## Afficher l'objet twitter API
#api


# #### Ma timeline

# In[3]:


#public_tweets = api.home_timeline()
# foreach through all tweets pulled
#for tweet in public_tweets:
   # printing the text stored inside the tweet object
#   print(tweet.user.screen_name,"a Twitté:",tweet.text)


# #### Recherche d'un profil particulier (Ici Nobel Price, compte offciel)

# In[4]:


#### Recherche de profil tweeter  (user timeline)

#api = tweepy.API(auth)

# The Twitter user who we want to get tweets from Nobel price

#name = "nobelprize"

# Number of tweets to pull

#tweetCount = 20

# Calling the user_timeline function with our parameters
#results = api.user_timeline(id=name, count=tweetCount, lang="fr")

# foreach through all tweets pulled
#for tweet in results:
   # printing the text stored inside the tweet object
#   print(tweet.text)


# #### Recherche d'un mots clé en particulier (Requête twitter ou Hashtag)

# In[5]:


# Creating the API object while passing in auth information
api = tweepy.API(auth)

# Le mots a cherché
query = "#France"
# Langue
language = "fr"

# Calling the user_timeline function with our parameters
results = api.search(q=query, lang=language)

# foreach through all tweets pulled
#for tweet in results:
   # printing the text stored inside the tweet object
#   print(tweet.user.screen_name,"Tweeted:",tweet.text)
result2 = []
for tre in results:
    result2.append(results)


# In[6]:


#for tweet in results:
   # printing the text stored inside the tweet object
#   print(tweet.user.screen_name,"Tweeted:",tweet.text)


# #### Récuperer les 100 derniers tweets de 8 journaux

# In[7]:


result = []
liste = ["@CNEWS", "@BFMTV", "@lemondefr", "@le_Parisien", "@LCI", "@franceinfo", "@afpfr", "@Le_Figaro"]
for ele in liste:
    result.append(api.user_timeline(ele, count = 100))
#for i in result:
#    for tweet in i:
#        print(tweet.text)
    
#len(result)


# In[8]:


#for i in result:
#    for tweet in i:
#        print(tweet.text)


# In[9]:


result3=result#+result2


# In[10]:


#result3


# #### Nettoyage des données

# In[11]:


#pip install nltk
#pip install textblob
import tweepy as tw
#import pandas as pd
import matplotlib.pyplot as plt
#import seaborn as sns
#import itertools
#import collections
import nltk
from nltk.corpus import stopwords
import re
#import networkx
#from textblob import TextBlob

import warnings
warnings.filterwarnings("ignore")

##### On définie une fonction de nettoyage des données

def remove_url(txt):
    """Remplace les url trouvée par le caractère vide " "
    

    Parametre
    ----------
    txt : string
        la variable string que l'on soutaite remplacer

    Sortie
    -------
    
    Le fichier nettoyé des url
    
    """

    #return " ".join(re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", txt).split())
    return " ".join(re.sub('http\w+:\/\/\S+', '', txt).split())


# On retire les caractères 
tweets_sans_urls = [remove_url(tweet.text)  for i in result3 for tweet in i]


# In[12]:


mots_dans_tweets = [tweet.lower().split() for tweet in tweets_sans_urls]


# #### Retrait des mots 

# In[13]:


#### Téléchargement NLTK
nltk.download('stopwords')
stop_words = set(stopwords.words('french'))

#list(stop_words)[0:25]


# In[14]:


tweet_sans_sw = [[mots for mots in mots_tweet if not mots in stop_words]
                 for mots_tweet in mots_dans_tweets]


# In[15]:
liste_stop_words = list(stop_words)

a_retirer = a_retirer = ["rt", "a", ":", "surtout", "si", "depuis", "de", "@cnews_sport:", "@lefigaroabonnes:", "le", "c'est","selon", "comme", "alors", "d'un", "d'une", "lefigaroabonnes", "tout", "tous", "@olivierveran:", "olivier véran", "va","ça", "entre"]+ liste_stop_words

#### On réutilise double listes

tweet_avec_mots_bannnis = [[mots for mots in mots_tweet if mots  not in a_retirer  ]
                 for mots_tweet in tweet_sans_sw]


# In[16]:


#tweet_avec_mots_bannnis


# #### WordCloud
# 
# 
# 

# In[17]:


#pip install wordcloud
import os.path
from wordcloud import WordCloud

#premiere maniere:
a=""
for mots in tweet_avec_mots_bannnis:
  a=a+" ".join(mots)
#On classifie en fonction de leurs importance les mots de tweet_sans_sw.txt avec Wordcloud
wordcloud = WordCloud(max_font_size=40).generate(a)

#Deuxieme maniere :
#on importe les mots de tweet_sans_sw dans le txt
#f = open("tweet_sans_sw.txt", "w")
#for mots in tweet_sans_sw:
#    f.write("\n".join(mots))
#wordcloud = WordCloud(max_font_size=40).generate(open(path.join(d, 'tweet_sans_sw.txt')).read())
#-----------------------------------------

#On affiche sur une image
import matplotlib.pyplot as plt
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
##plt.figure()
#plt.show()


# In[18]:


wordcloud.to_file('/home/venus/Wordcloud twitter/mots_du_jour.png')

wordcloud.to_file('/home/venus/Git_repo/mots_du_jour.png')
# In[ ]:




# In[ ]:





# In[ ]:





# In[ ]:




