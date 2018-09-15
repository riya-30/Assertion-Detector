import pandas as pd
import seaborn as sns
from sklearn.linear_model import LogisticRegression
import numpy as np
import matplotlib.pyplot as plt

'''assIndex = []  
assIndex.extend(range(3,72))
assIndex.extend([277, 280])

trainX = np.identity(284, int)
trainy = np.zeros(284, int)   
for i in assIndex:
        trainy[i] = 1
        
np.savetxt("trainX.csv", trainX, fmt = '%d', delimiter = ',')
np.savetxt("trainy.csv", trainy, fmt = '%d', delimiter = ',')'''

train = pd.read_csv("C:/Users/Rohan Challana/train.csv", header=None)
#output = pd.read_csv("C:/Users/RishG/Desktop/trainy.csv", header= None)
X_test = pd.read_csv("C:/Users/Rohan Challana/testX.csv", header=None)         #question need to be answered

ft_cols = list(range(284))
X_train = train[ft_cols]
y_train = train[284]
print(train,ft_cols,X_train,y_train)
logreg = LogisticRegression()

logreg.fit(X_train, y_train)

y_pred = logreg.predict(X_test)

f, (ax1) = plt.subplots(1, 1, figsize=(8, 6), sharex=True)
x = np.array(['Not Assertion', 'Assertion'])
sns.countplot(y_pred, palette="BuGn_d", ax=ax1)
ax1.set_ylabel("No. of tweets")
ax1.set_xlabel("Not Assertion/Assertion")

c=0
cnt = 0
l = []
for i in y_pred:
    if i==1:
        c+=1
        l.append(cnt) 
    cnt +=1
print("No. of assertions = %d" %c)