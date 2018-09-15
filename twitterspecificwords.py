import nltk
from collections import defaultdict
import os
import json
class Tweet(object):
    def __init__(self,freq,no):
        self.freq=freq
        self.no=no
fileArray = os.listdir('C:/Users/Rohan Challana/Json'+'/')
tweets=[]
for file in fileArray:
    f = open('C:/Users/Rohan Challana/Json'+'/'+file, 'r', encoding='utf-8')
    for line in f:
        jsonStruct = json.loads(line)
        if 'text' in jsonStruct:
            tweet = jsonStruct['text']
            "print (tweet)"
            tweets.append(tweet)
            #NOw do what you want with this tweet
f.close()
no=1
print("Tweet No   @     #     RT")
for line in tweets:
    word=nltk.word_tokenize(line)
    print(str(no),end=''),
    if '@' in word:
        print("          1",end=''),
    else:
        print("          0",end=''),
    if '#' in word:
        print("     1",end=''),
    else:
        print("     0",end=''),
    if 'RT'==word[0]:
        if(word[1]=='@'):
            print("     1",end=''),
        else:
            print("     0",end=''),
    print("\n")
    no+=1
