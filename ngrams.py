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
words=[]
word=[]
d="!£$%^&*()--_=+[]{};''#,./:@~<>?//""...''``"
for line in tweets:
    word=nltk.word_tokenize(line)
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
    for word in i:
        if dictu[word]>=5:
            obj=Tweet(word,no)
            dictfu.append(obj)
    a=i[0]
    for word in i[1:]:
        if dictb[a+" "+word]>=5:
            obj=Tweet(a+" "+word,no)
            dictfb.append(obj)
            a=word
    a=i[0]
    b=i[1]
    for word in i[2:]:
        if dictt[a+" "+b+" "+word]>=5:
            obj=Tweet(a+" "+b+" "+word,no)
            dictft.append(obj)
            a=b
            b=word
    no+=1
f=open("ngrams.txt",'w')
print("Unary Ngrams:Words and Their correspoding Tweet No")
for i in dictfu:
    print(i.freq+"  "+str(i.no))
    d=i.freq+"  "+str(i.no)
    f.write(d)
print("\n")
print("Binary Ngrams:Words and Their correspoding Tweet No")
for i in dictfb:
    print(i.freq+"  "+str(i.no))
    f.write(i.freq+"  "+str(i.no))
print("\n")
print("Ternary Ngrams:Words and Their correspoding Tweet No")
for i in dictft:
    print(i.freq+"  "+str(i.no))
    f.write(i.freq+"  "+str(i.no))
f.close()