# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 20:04:41 2020

@author: Hui
"""

import urllib.request, json 
import pandas as pd
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re
import os


with urllib.request.urlopen("https://s3.amazonaws.com/oneonepsilon-database/database.json") as url:
    database = json.loads(url.read().decode())
    
videolist = database['videos']
df = pd.DataFrame(videolist)
title_df = df[['youtubeVideoId','ourTitle']]

####  remove punctuation and lower the string in title
for index, row in title_df.iterrows():
    row['ourTitle'] = [char for char in row['ourTitle'] if char not in string.punctuation]
    row['ourTitle'] = ''.join(row['ourTitle'])
    row['ourTitle'] = row['ourTitle'].lower()
    
### get rid of all the integer values
def numberfilter(samplelist):
    for token in samplelist:
        try:
            int(token)
            continue # Skip the numbers
        except ValueError:
            yield token 

### tokenize and stopwords   getting rid of interger
for index, row in title_df.iterrows():
    row['ourTitle'] = word_tokenize(row['ourTitle'])
    row['ourTitle'] = [word for word in row['ourTitle'] if word not in stopwords.words('english')]
    row['ourTitle'] = list(numberfilter(row['ourTitle']))

##### THIS IS FOR READING THE CLEANED CAPTION FILE IN LOCAL
##### REMEMBER TO CHANGE TO YOUR OWN PATH
findtxt = re.compile(r'[0-9a-zA-Z]+\.txt')
findtxt.findall(r'new.txt*****new.txt')
os.chdir('E:/UQ/DATA7901/Project/Caption after clean(stopword)/')
filelist = os.listdir('E:/UQ/DATA7901/Project/Caption after clean(stopword)/')

#### creating an empty dataframe
result =pd.DataFrame(columns=('youtubeVideoId','Text'))
#### putting all text into a data frame
for i in filelist: 
    with open(i, encoding='gb18030', errors='ignore') as file:
        textString = file.read().replace('/n','')
    result = result.append(pd.DataFrame({'youtubeVideoId':[i],'Text':[textString]}))

#### getting rid of ".txt" in the YouTube video ID
for index, row in result.iterrows():
    row['youtubeVideoId'] = row['youtubeVideoId'][:-4]
    
### combine two dataframes, should have 1398 rows 
combine = pd.merge(result, title_df, on = 'youtubeVideoId')

### tokenize the text
for index, row in combine.iterrows():
    row['Text'] = word_tokenize(row['Text'])
    row['Text'] = list(numberfilter(row['Text']))

### add text length
list1 = []
for index, row in combine.iterrows():
    list1.append(len(row['Text']))
combine = combine.assign(TextTotallen = list1)

def get_index(titletimes):
    appeartime = 0
    for i in row['ourTitle']:
        count = row['Text'].count(i)
        appeartime += count
    return appeartime

#### add title appeared time
list2 = []
for index, row in combine.iterrows():
    list2.append(get_index(row['ourTitle']))
combine = combine.assign(appeartime = list2)

# new index
combine['index'] = combine['appeartime']/combine['TextTotallen']


print(combine["index"].mean())
