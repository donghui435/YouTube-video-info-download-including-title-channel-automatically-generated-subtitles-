import pandas as pd
from youtube_transcript_api import YouTubeTranscriptApi
import os.path

ID = pd.read_csv('Sampledata.csv')
ID_list = ID['Video_ID'].tolist()

# You can adjust your files output path 
txt_save_path = 'C:/Users/User/Captions_download' 

for ID in ID_list:
    try: 
        # I'm using all english video IDs right here in the data set, if you want to other language videos, you can change the language
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
