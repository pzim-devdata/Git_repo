#!/usr/bin/env python
# coding: utf-8

#pip install tweepy
#pip install nltk
#pip install wordcloud

import os.path
from wordcloud import WordCloud
import tweepy
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
import re

#### On remplace ici les valeurs des Key, secret et Token par celle de l'application crée sur l'environnement twitter :

CONSUMER_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXx'
CONSUMER_SECRET = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
OAUTH_TOKEN = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx'
OAUTH_TOKEN_SECRET = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

##### Connexion à l'API :

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
#  Token et secret :
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
# Création de l'API :
api = tweepy.API(auth) 


#### Recherche d'un mots clé en particulier (Requête twitter ou Hashtag) :

# Le mots a cherché
query = "#France"
# Langue
language = "fr"

# Appelle de l'API
results = api.search(q=query, lang=language)

result = []
for tre in results:
    result.append(results)

# Affichage des résultats :
#for tweet in results:
   # printing the text stored inside the tweet object
#   print(tweet.user.screen_name,"Tweeted:",tweet.text)

#### Récuperer les 100 derniers tweets de 8 journaux :

result2 = []
liste = ["@CNEWS", "@BFMTV", "@lemondefr", "@le_Parisien", "@LCI", "@franceinfo", "@afpfr", "@Le_Figaro"]
for ele in liste:
    result2.append(api.user_timeline(ele, count = 100))

# Affichage des résultats :
#for i in result:
#    for tweet in i:
#        print(tweet.text)
    

# Concaténation des résultats de recherche :
result3=result#+result2


#### Nettoyage des données :

import tweepy as tw
import warnings
warnings.filterwarnings("ignore")

# On définie une fonction de nettoyage des données (retrait des url et des caractéres spéciaux) :

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
    return " ".join(re.sub('http\w+:\/\/\S+', '', txt).split())

# On retire les caractères spéciaux et les url de result3 :

tweets_sans_urls = [remove_url(tweet.text)  for i in result3 for tweet in i]

# On crée la liste des mots :

mots_dans_tweets = [tweet.lower().split() for tweet in tweets_sans_urls]


# Retrait des mots non pertinents avec nltk :

# Téléchargement NLTK
nltk.download('stopwords')
stop_words = set(stopwords.words('french'))

# Retrait des mots non pertinents :

tweet_sans_sw = [[mots for mots in mots_tweet if not mots in stop_words]
                 for mots_tweet in mots_dans_tweets]


liste_stop_words = list(stop_words)

a_retirer = ["rt", "a", ":", "surtout", "si", "depuis", "de", "@cnews_sport:", "@lefigaroabonnes:", "le", "c'est","selon", "comme", "alors", "d'un", "d'une", "lefigaroabonnes", "tout", "tous", "@olivierveran:", "olivier véran", "va","ça", "entre"]+ liste_stop_words

# On réutilise une double listes pour retirer les mots non pertinents:

tweet_avec_mots_bannnis = [[mots for mots in mots_tweet if mots  not in a_retirer  ]
                 for mots_tweet in tweet_sans_sw]


#### WordCloud : Création de l'image finale :

#Premiere maniere avec une phrase :
a=""
for mots in tweet_avec_mots_bannnis:
  a=a+" ".join(mots)
#On classifie en fonction de leurs importance les mots de tweet_avec_mots_bannnis.txt avec Wordcloud
wordcloud = WordCloud(max_font_size=40).generate(a)

#Deuxieme maniere on crée un fichier txt :
#on importe les mots de tweet_sans_sw dans le txt
#f = open("tweet_avec_mots_bannnis.txt", "w")
#for mots in tweet_avec_mots_bannnis:
#    f.write("\n".join(mots))
#wordcloud = WordCloud(max_font_size=40).generate(open(path.join(d, 'tweet_avec_mots_bannnis.txt')).read())
#-----------------------------------------

# On affiche l'image Wordcloud :
import matplotlib.pyplot as plt
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
##plt.figure()
#plt.show()

# Enfin on sauvagarde l'image Wordcloud :
wordcloud.to_file('/home/venus/Wordcloud twitter/mots_du_jour.png')

wordcloud.to_file('/home/venus/Git_repo/mots_du_jour.png')


#### La timeline perso de mon compte :

#public_tweets = api.home_timeline()
# foreach through all tweets pulled
#for tweet in public_tweets:
   # printing the text stored inside the tweet object
#   print(tweet.user.screen_name,"a Twitté:",tweet.text)


#### Recherche d'un profil particulier (Ici Nobel Price, compte offciel)

#api = tweepy.API(auth)

#name = "nobelprize"

# Nombre de tweets à chercher :

#tweetCount = 20

# Appelle de l'API :

#results = api.user_timeline(id=name, count=tweetCount, lang="fr")

# Affichage des résultats
#for tweet in results:
   # printing the text stored inside the tweet object
#   print(tweet.text)





