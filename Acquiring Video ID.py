# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 13:26:25 2020

@author: HUI
"""

import urllib.request, json 
import pickle

### the url includes a json file with all video ids on one on Epsilon
with urllib.request.urlopen("https://s3.amazonaws.com/oneonepsilon-database/database.json") as url:
    database = json.loads(url.read().decode())
    
count = 0
for videoID in database['videos']:
    print(videoID['youtubeVideoId'])
    count = 1 + count 
print(count) ### there are 1504 video id in total

### extract video id and put it in a list
VideoID_list = []
for videoID in database['videos']:
    VideoID_list.append(videoID['youtubeVideoId'])
    
with open("VideoID.txt", "wb") as fp:   #Pickling
    pickle.dump(VideoID_list, fp)