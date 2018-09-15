import nltk
from collections import defaultdict
import os
import json
import re
rish = open('test.txt', 'w',  encoding = 'utf-8')
fileArray = os.listdir('C:/Users/Rohan Challana/Pos tagger'+'/')
tweets=[]
p=1
wordm=""
d="abcdeffghijklmnopqrstuvwxyxABCDEFGHIJKLMNOPQRSTUVWXY'Z"
for file in fileArray:
    f = open('C:/Users/Rohan Challana/Pos Tagger'+'/'+file, 'r', encoding='utf-8')
    for line in f:
        if line=='\n':
            wordm+="\n"
            tweets.append(wordm)
            wordm=""
        else:
            m= line.split('\t')
            for i in m[0]:
                if i in d:
                    wordm+=i
            wordm+=" "
    f.close()
words=[]
word=[]
wordd=[]
wordf=[]
for line in tweets:
    word=line.split(' ')
    while "http" in word:
        inx=word.index("http")
        word=word[:inx]+word[inx+3:]
    while "https" in word:
        inx=word.index("https")
        word=word[:inx]+word[inx+3:]
    wordf=""
    for j in word:
        if j in d:
            pass
        else:
            wordf+=" "+j
    "print(wordf) tweets without punctuations"
    words.append(wordf)
wordsf=[]
dictu={}
dictu=defaultdict(lambda: 0,dictu)
dictb={}
dictb=defaultdict(lambda: 0,dictb)
dictt={}
dictt=defaultdict(lambda: 0,dictt)
no=1
for j in words:
    j=j.lower()
    i=j.split()
    for word in i:
        dictu[word]+=1
    a=i[0]
    for word in i[1:]:
        dictb[a+" "+word]+=1
        a=word
    a=i[0]
    b=i[1]
    for word in i[2:]:
        dictt[a+" "+b+" "+word]+=1
        a=b
        b=word
dictfu=[]
dictfb=[]
dictft=[]
no=1
for j in words:
    j=j.lower()
    i=j.split()
    rish.write(str(no)+"\n")
    for word in i:
        if dictu[word]>=3:
            rish.write(word+"\n")
    a=i[0]
    for word in i[1:]:
        if dictb[a+" "+word]>=3:
            rish.write(a+" "+word+"\n")
            a=word
    a=i[0]
    b=i[1]
    for word in i[2:]:
        if dictt[a+" "+b+" "+word]>=3:
            rish.write(a+" "+b+" "+word+"\n")
            a=b
            b=word
    rish.write("\n")
    no+=1
rish.close()