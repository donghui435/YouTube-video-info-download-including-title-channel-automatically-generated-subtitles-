# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 13:53:48 2020

@author: HUI
"""


import os.path
import requests
import json
import pickle


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