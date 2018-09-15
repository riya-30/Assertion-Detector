import nltk
from collections import defaultdict
import os
import json
import re
import numpy as np
rish = open('semantic.txt', 'w',  encoding = 'utf-8')
final={}

def speechactverbs(lines):
    p=1
    print("Speechactverbs Results:")
    f=open("NEWstemmedSpeechAct.txt",'r', encoding = 'utf-8')
    sourcelines=f.readlines()
    i=1
    while(lines[i]!="0"):
        final[p]=list(np.zeros(284, int))
        while(lines[i]!="\n"):
            flag=0
            j=0
            for line in sourcelines:
                if line==lines[i]:
                    print(str(p)+" Yes "+lines[i][:-1])
                    flag=1
                    break
                j+=1
            if flag==1:
                final[p][j]=1
            if flag!=1:
                print(str(p)+" No "+lines[i][:-1])
            if lines[i+1]=="0":
                break
            else:
                i+=1
        if lines[i+1]!="0":
            i+=2
        else:
            i+=1
        p+=1
    f.close()

def twitterspecificwords():
    fileArray = os.listdir('C:/Users/Rohan Challana/Json'+'/')
    tweets=[]
    p=1
    for file in fileArray:
        f1 = open('C:/Users/Rohan Challana/Json'+'/'+file, 'r', encoding='utf-8')
        for line in f1:
            jsonStruct = json.loads(line)
            if 'entities' in jsonStruct:
                if 'user_mentions' in jsonStruct['entities']:
                    if jsonStruct['entities']['user_mentions']:
                        final[p][276]=1
                        print(str(p)+" "+str(276))
                        for i in jsonStruct['entities']['user_mentions']:
                            if "text" in jsonStruct:
                                    if jsonStruct["text"][i["indices"][0]-3:i["indices"][0]]=="RT ":
                                        final[p][277]=1
                                        print(str(p)+" "+str(277))
                            if i["indices"][0]==3:
                                if "text" in jsonStruct:
                                    if jsonStruct["text"][0:3]=="RT ":
                                        final[p][280]=1
                                        print(str(p)+" "+str(280))
                            elif i["indices"][0]==0:
                                final[p][279]=1
                                print(str(p)+" "+str(279))

                if 'hashtags' in jsonStruct['entities']:
                    if jsonStruct['entities']['hashtags']:
                        final[p][275]=1
                        print(str(p)+" "+str(275))
                        for i in jsonStruct['entities']['hashtags']:
                            if i["indices"][0]==0:
                                final[p][278]=1
                                print(str(p)+" "+str(278))
            p+=1

tweets=[]
"""fileArray = os.listdir('C:/Users/Rohan Challana/Json'+'/')
for file in fileArray:
    f1 = open('C:/Users/Rohan Challana/Json'+'/'+file, 'r', encoding='utf-8')
    for line in f1:
        jsonStruct = json.loads(line)
        if 'text' in jsonStruct:
            tweet = jsonStruct['text']
            tweets.append(tweet)
    f1.close()"""
f2=open("bb_verbsstemmed.txt",'r', encoding = 'utf-8')
tweets2=f2.readlines()
speechactverbs(tweets2)
f2.close()
twitterspecificwords()