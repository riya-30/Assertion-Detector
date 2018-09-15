import nltk
from collections import defaultdict
import os
import json
import re
import numpy as np
rish = open('semantic.txt', 'w',  encoding = 'utf-8')
final={}

def opinion(lines):
    p=1
    print("Opinion Results:")
    f=open("Opinion Words final.txt",'r', encoding = 'utf-8')
    sourcelines=f.readlines()
    for line in lines:
        final[p]=list(np.zeros(284, int))
        word=nltk.word_tokenize(line)
        for char in word:
            if char.upper()+"\n" in sourcelines:
                print(str(p)+" Yes")
                final[p][0]=1
                break
        else:
            print(str(p)+" No")
        p+=1
    print("\n")
    f.close()

def vulgar(lines):
    p=1
    print("Vulgar Results:")
    f=open("Vulgar.txt",'r', encoding = 'utf-8')
    sourcelines=f.readlines()
    for line in lines:
        word=nltk.word_tokenize(line)
        for char in word:
            if char.lower()+" \n" in sourcelines:
                print(str(p)+" Yes"+char)
                final[p][1]=1
                break
            else:
                print(str(p)+" No")
        p+=1
    print("\n")
    f.close()

def emoticon(lines):
    p=1
    print("Emoticon Results:")
    f=open("emoticon final.txt",'r', encoding = 'utf-8')
    sourcelines=f.readlines()
    for line in lines:
        for char in sourcelines:
            if  char[:-1] in line:
                print(str(p)+" Yes "+char[:-1])
                final[p][2]=1
                break
        else:
            print(str(p)+" No")
        p+=1
    print("\n")
    f.close()

def speechactverbs(lines):
    p=1
    print("Speechactverbs Results:")
    f=open("NEWstemmedSpeechAct.txt",'r', encoding = 'utf-8')
    sourcelines=f.readlines()
    i=1
    while(lines[i]!="0"):
        while(lines[i]!="\n"):
            flag=0
            j=3
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

def punctuation(lines):
    p=1
    print("Punctuation Results:")
    for line in lines:
        word=nltk.word_tokenize(line)
        if '?' in word:
            print(str(p)+" Yes ?")
            final[p][273]=1
        elif '!' in word:
            print(str(p)+" Yes !")
            final[p][274]=1
        else:
            print(str(p)+" No")
        p+=1
    print("\n")

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

def abbreviation(lines):
    p=1
    print("Abbreviation Results:")
    f=open("Abbreviation.txt",'r', encoding = 'utf-8')
    sourcelines=f.readlines()
    for line in lines:
        word=nltk.word_tokenize(line)
        for char in word:
            if char+"\n" in sourcelines:
                print(str(p)+" Yes "+char)
                final[p][281]=1
                break
        else:
            print(str(p)+" No")
        p+=1
    print("\n")
    f.close()

def partofspeech(lines):
    p=1
    print("Part Of Speech Results:")
    i=0
    while i!=len(lines):
        while lines[i][0]!="\n":
            word=nltk.word_tokenize(lines[i])
            if word[len(word)-2]=='A':
                print(str(p)+" Yes "+word[1])
                final[p][282]=1
            elif word[len(word)-2]=='!':
                print(str(p)+" Yes "+word[1])
                final[p][283]=1
            i+=1
        i+=1
        p+=1

tweets=[]
fileArray = os.listdir('C:/Users/Rohan Challana/Json'+'/')
for file in fileArray:
    f1 = open('C:/Users/Rohan Challana/Json'+'/'+file, 'r', encoding='utf-8')
    for line in f1:
        jsonStruct = json.loads(line)
        if 'text' in jsonStruct:
            tweet = jsonStruct['text']
            tweets.append(tweet)
    f1.close()

opinion(tweets)
vulgar(tweets)
emoticon(tweets)
punctuation(tweets)
twitterspecificwords()
abbreviation(tweets)

f2=open("bb_verbsstemmed.txt",'r', encoding = 'utf-8')
tweets2=f2.readlines()
speechactverbs(tweets2)
f2.close()

tweets3=[]
fileArray1 = os.listdir('C:/Users/Rohan Challana/Pos Tagger'+'/')
for file in fileArray1:
    f3 = open('C:/Users/Rohan Challana/Pos Tagger'+'/'+file, 'r', encoding='utf-8')
    for line in f3:
        tweets3.append(line)
    f3.close()
partofspeech(tweets3)

f=open("features.csv",'w')
for i in final.keys():
    for j in final[i][:-1]:
        f.write(str(j)+",")
    f.write(str(final[i][-1]))
    f.write("\n")
f.close()
