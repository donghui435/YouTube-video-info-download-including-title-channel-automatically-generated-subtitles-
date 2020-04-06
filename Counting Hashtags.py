# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 21:55:35 2020

@author: User
"""
import urllib.request, json 
import pandas as pd


with urllib.request.urlopen("https://s3.amazonaws.com/oneonepsilon-database/database.json") as url:
    database = json.loads(url.read().decode())

"""  
print(json.dumps(database, indent = 4))  ###more clear structure look
database.keys() ###5 keys
dict_keys(['featuredURLs', 'mathObjects', 'mathObjectLinks', 'videos', 'snippets']

take some useful attributes to form a new dict
youtubeVideoId;  durationSec; hashTags(under videos)

"""
videolist = database['videos']
df = pd.DataFrame(videolist)
df_new = df[['youtubeVideoId', 'hashTags',  'ourTitle']]

list1 = df_new['hashTags'].tolist()
greatlist = []
for i in list1:
    greatlist += i 

### len(greatlist) is 2121

def get_counts(sequence):
    counts = {}
    for i in sequence:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    return counts

count_dict = get_counts(greatlist)
sort_d = sorted(count_dict.items(), key = lambda k: k[1], reverse=True)
print(sort_d[:50])  ### top 50 hashtags with highest appearance
