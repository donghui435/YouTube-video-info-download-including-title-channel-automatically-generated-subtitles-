# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 13:53:48 2020

@author: HUI
"""


import os.path
import requests
import json
import pickle
from urllib.request import urlopen 


### Key.txt includes my YouTube API key
file = open("Key.txt") 
key = (file.read()).rstrip("\n")

# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
#https://cloud.google.com/console
DEVELOPER_KEY = key
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

with open("VideoID.txt", "rb") as fp:   # Unpickling
    ID_list = pickle.load(fp)
    
json_save_path = 'E:/UQ/DATA7901/Project/video_info'  ##set your own path

### download video info    Output is stored in Data/video_info
for ID in ID_list:
    url = "https://www.googleapis.com/youtube/v3/videos?part=snippet&id={id}&key={api_key}"
    r = requests.get(url.format(id=ID, api_key=DEVELOPER_KEY))
    data = r.json()
    filename = os.path.join(json_save_path, ID + '.json')
    with open(filename,'a',encoding='utf-8') as outfile:
        json.dump(data,outfile,ensure_ascii=False)
        outfile.write('\n')
        
### require video views and likes for one video
SpecificVideoID = 'mLeNaZcy-hE' ###this is a random video ID
SpecificVideoUrl = 'https://www.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails%2Cstatistics&id='+SpecificVideoID+'&key='+DEVELOPER_KEY
response = urlopen(SpecificVideoUrl) #makes the call to a specific YouTube
videos = json.load(response) #decodes the response so we can work with it
videoMetadata = [] #declaring our list
for video in videos['items']: 
    if video['kind'] == 'youtube#video':
        print("Upload date:        "+video['snippet']['publishedAt'])    # Here the upload date of the specific video is listed
        print("Number of views:    "+video['statistics']['viewCount']) # Here the number of views of the specific video is listed
        print( "Number of likes:    "+video['statistics']['likeCount'])  # etc
        print ("Number of dislikes: "+video['statistics']['dislikeCount'])
        print ("Number of favorites:"+video['statistics']['favoriteCount'])
        print ("Number of comments: "+video['statistics']['commentCount'])
        print ("\n")



