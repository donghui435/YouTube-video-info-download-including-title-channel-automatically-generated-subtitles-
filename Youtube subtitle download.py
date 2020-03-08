# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 13:32:46 2020

@author: HUI
"""


from youtube_transcript_api import YouTubeTranscriptApi
'''
YouTubeTranscriptApi is a python API which allows you to get the
transcripts/subtitles for a given YouTube video
writen by jdepoix
https://github.com/jdepoix/youtube-transcript-api.git
'''
import os.path
import pickle

### using the file created from Acquiring video ID
with open("VideoID.txt", "rb") as fp:   # Unpickling
    ID_list = pickle.load(fp)
    
    
    
###txt file output
txt_save_path = 'E:/UQ/DATA7901/Project/subtitles' ##set your own path

### some videos doesn't have any subtitles and will be labeled as Null+videoID
### Output is stored in Data/Caption
for ID in ID_list:
    try: 
        caption = YouTubeTranscriptApi.get_transcript(video_id=ID, languages=['en'])
        caption1 = [i['text'] for i in caption]
        caption_new = ''.join(caption1)
        file_name = os.path.join(txt_save_path, ID + '.txt')
        f = open(file_name, "w")
        f.write(caption_new)
        f.close()
    except:
        file_name = os.path.join(txt_save_path, 'Null_' + ID + '.txt')
        f = open(file_name, "w")
        f.close()