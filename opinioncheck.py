from collections import defaultdict
f=open("Abbreviation.txt",'r')
words=f.readlines()
dict={}
dict=defaultdict(lambda: 0,dict)
for word in words:
    dict[word]+=1
print(dict)
c=1
#f1=open("emoticon final.txt",'w')
for i in dict.values():
    if i>1:
        print("yes")
#f1.close()
f.close()