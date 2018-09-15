from collections import defaultdict
from math import log
f1=open("dependency_tree.txt",'r', encoding = 'utf-8')
f2=open("annotated (1).txt",'r', encoding = 'utf-8')
f3=open("600dependency_tree.txt",'w', encoding = 'utf-8')
lines1=f1.readlines()
lines2=f2.readlines()
p=1
count={}
count=defaultdict(lambda: 0,count)
prob={}
prob=defaultdict(lambda: 0,prob)
i=1
j=0
while j!=600:
    while lines1[i]!="\n":
        if lines2[j]!='\n':
            prob[lines1[i][:-1]]+=(int(lines2[j][:-1]))
            count[lines1[i][:-1]]+=1
        else:
            lines2[j]='0\n'
            prob[lines1[i][:-1]]+=(int(lines2[j][:-1]))
            count[lines1[i][:-1]]+=1
        i+=1
    i+=2
    j+=1
for i in prob.keys():
    prob[i]/=count[i]
for i in prob.keys():
    print(i,prob[i])
for i in prob.keys():
    if prob[i]!=0 and (1-prob[i])!=0:
        x=-prob[i]*log(prob[i],2)-((1-prob[i])*log((1-prob[i]),2))
        f3.write(i+" "+str(x))
        f3.write("\n")
    else:
        f3.write(i+" "+str(prob[i]))
        f3.write("\n")
#print(str(prob.keys())+" "+str(prob.values()))
f1.close()
f2.close()
f3.close()