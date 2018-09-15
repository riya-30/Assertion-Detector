import os
import json
fileArray = os.listdir('C:/Users/Rohan Challana/Json'+'/')
tweets=[]
c=1
k=0
for file in fileArray:
    f1 = open('C:/Users/Rohan Challana/Json'+'/'+file, 'r', encoding='utf-8')
    for line in f1:
        jsonStruct = json.loads(line)
        if 'entities' in jsonStruct:
            if 'user_mentions' in jsonStruct['entities']:
                if jsonStruct['entities']['user_mentions']:
                    print(jsonStruct['entities']['user_mentions'])

        c+=1
            #if jsonStruct['retweeted'] is True:
                #if 'text' in jsonStruct:
                  #  tweet = jsonStruct['text']
                   # tweets.append(tweet)
    f1.close()
    #print(tweets