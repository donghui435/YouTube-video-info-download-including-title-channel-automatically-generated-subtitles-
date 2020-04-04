
import re
import os
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.corpus import words

findtxt = re.compile(r'[0-9a-zA-Z]+\.txt')
findtxt.findall(r'new.txt*****new.txt')

os.chdir('E:/UQ/DATA7901/Project/Caption/')
filelist = os.listdir('E:/UQ/DATA7901/Project/Caption/')

### hash table impllemtation of dictionary
My_dict = {}
for i in words.words():
    My_dict[i] = i
    
### read file
for i in filelist: 
    with open(i, encoding='gb18030', errors='ignore') as file:
        textString = file.read().replace('/n','')
    
    ### eliminate the punctuation in form of characters
    textString = [char for char in textString if char not in string.punctuation]
    textString = ''.join(textString)
    textString = textString.lower()
    
    ### tokenize
    textString_token = word_tokenize(textString)
    
    ### stopwords eliminating 1st time
    textString_stop = [word for word in textString_token if word not in stopwords.words('english')]
    
    ### Spelling checking and dividing two connected words
    list1 = []
    for word in textString_stop:
        if word in My_dict:
            list1.append(word)
        else:
            list2 = []
            count_j = 0
            for j in range(1,len(word)):
                if word[:j] in My_dict and word[j:] in My_dict:
                    list2.append(word[:j])
                    list2.append(word[j:])
                    count_j += 1
            if count_j == 1:
                list1.extend(list2)
                
    ### eliminate stopwords 2nd time
    clean_sentence = [word for word in list1 if word.lower() not in stopwords.words('english')]
    
    ### write into new file
    new_path = 'E:/UQ/DATA7901/Project/Caption after clean/'
    new_text = ' '.join(clean_sentence)
    file_name = os.path.join(new_path, i)
    f = open(file_name, 'w')
    f.write(new_text)
    f.close()
