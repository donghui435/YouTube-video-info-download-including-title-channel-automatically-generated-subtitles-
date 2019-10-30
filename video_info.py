import pandas as pd
import numpy as np
import os.path
import requests
import json

#this is the YouTube API key, you can apply your own API key
file = open("Key.txt") 
develop_key = (file.read()).rstrip("\n")

YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

ID = pd.read_csv('Sampledata.csv')
ID_list = ID['Video_ID'].tolist()

#set output file path
json_save_path = 'C:/Users/User/video_info'

#get the json file of video info
for ID in ID_list:
    url = "https://www.googleapis.com/youtube/v3/videos?part=snippet&id={id}&key={api_key}"
    r = requests.get(url.format(id=ID, api_key=develop_key))
    data = r.json()
    filename = os.path.join(json_save_path, ID + '.json')
    with open(filename,'a') as outfile:
        json.dump(data,outfile,ensure_ascii=False)
        outfile.write('\n')