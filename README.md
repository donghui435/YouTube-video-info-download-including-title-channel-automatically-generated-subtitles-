# YouTube video info download (including title/channel/autogmatically generated subtitles)

This repository demonstrates how to downnload YouTube video's subtitle and information using video ID. It also includes some subtitle cleaning process and NLP analysis.

## Video ID dataset
The data this project using is from One On Epsilon. This is the data file URL which is in a json format:
https://s3.amazonaws.com/oneonepsilon-database/database.json
There are 1504 video IDs in total, including 106 null-subtitle files.
All the video IDs are stored at file VideoID.txt which has been Pickle serialized. So do remember unpickling when you use the data.
```
with open("VideoID.txt", "rb") as fp:   # Unpickling
    ID_list = pickle.load(fp)
```
## Install packages

The subtitles download is using youtube-transcript-api function created by jdepoix, links below include the package install intructions and the original repository:
https://pypi.org/project/youtube-transcript-api/
https://github.com/jdepoix/youtube-transcript-api

For the video info downloading, you need to apply your own YouTube Data API key in order to have access. Link below shows the instruction to apply YouTube Data API(you will need to have an google account):
https://console.developers.google.com/

## Subtitle part

The code is using data format of YouTube video ID which is a single column attribute
It will output the sustitle in txt format for each video, and if the video has no subtitle, the output will be null + the video ID
example: FGn2jtCjyvo.txt
         Null_0A83skSAxKI.txt
Each txt file will be a text string and they are stored at Data/Caption
## Video info part
This code is using the same dataset as the subtitle using, and output is a json file with all the information for each video, all the output is stored at Data/video_info


