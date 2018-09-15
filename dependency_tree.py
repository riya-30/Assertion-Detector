import nltk
from collections import defaultdict
import os
import json
import re
rish = open('dependency_tree.txt', 'w',  encoding = 'utf-8')
lines=[]
fileArray = os.listdir('C:/Users/Rohan Challana/Predict'+'/')
for file in fileArray:
    f = open('C:/Users/Rohan Challana/Predict'+'/'+file, 'r', encoding='utf-8')
    for line in f:
        lines.append(line)
#f=open("bb_01.predict",'r', encoding = 'utf-8')
#lines=f.readlines()
z1=int(lines[0][0])
p=1
i=0
while i!=len(lines):
    print(str(p))
    rish.write(str(p)+"\n")
    root=[]
    strings=[" "]
    final={}
    z=1
    x=0
    j=2
    while lines[i][0]!='\n':
        k1=0
        x=""
        while lines[i][k1]!='\t':
            x+=lines[i][k1]
            k1+=1
        x=int(x)
        z=""
        j=k1+1
        while lines[i][j]!="\t":
            z+=lines[i][j]
            j+=1
        strings.append(z)
        k=len(lines[i])-1
        while lines[i][k]!='\t':
            k-=1
            y=""
        while lines[i][k-1]!='\t':
            y=lines[i][k-1]+y
            k-=1
        y=int(y)
        if y in final.keys():
            final[y].append(x)
        else:
            final[y]=[x]
        if y==0:
            root.append(x)
        i+=1
    i+=1
    """print(final.keys(),final.values())
    print(root)"""
    list2=[]
    visited={}
    visited=defaultdict(lambda: 0,visited)
    for j in root:
        if j in final.keys():
            list2.append(j)
            while len(list2)!=0:
                s=list2.pop(0)
                if visited[s]!=1:
                    if s in final.keys():
                        for item in final[s]:
                            list2.append(item)
                            print(strings[s],strings[item])
                            rish.write(strings[s]+" "+strings[item]+"\n")
                        visited[s]=1
    visited1={}
    visited1=defaultdict(lambda: 0,visited1)
    list3=[]
    for j in root:
        if j in final.keys():
            list3.append(j)
            while len(list3)!=0:
                s=list3.pop(len(list3)-1)
                if visited1[s]!=1:
                    if s in final.keys():
                        for item in final[s]:
                            list3.append(item)
                            if item in final.keys():
                                for l in final[item]:
                                    print(strings[s],strings[item],strings[l])
                                    rish.write(strings[s]+" "+strings[item]+" "+strings[l]+"\n")
                        visited1[s]=1
    p+=1
    print("\n")
    rish.write("\n")
f.close()