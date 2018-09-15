import itertools
import numpy as np

"""f = open('trainX.csv', 'a')
g = open('trainy.csv', 'a')"""
X = np.zeros(285, int)
X[0] = 1
y = np.zeros(1, int)
for l in itertools.product(range(2),repeat = 2):
    for i in range(1,6):
        for x in itertools.combinations(range(70), i):
            k = np.zeros(285, int)
            k[278] = l[0]
            k[281]= l[1]
            for p in x:
                k[p] = 1
            X = np.vstack([X, k])
            y = np.vstack([y, 1])
            print(l)
            print(i)
            print(x)

np.savetxt("trainX1.csv", X, fmt = '%d', delimiter = ",")
np.savetxt("trainy1.csv", y, fmt = '%d', delimiter = ',')

'''for i in itertools.product(range(2), repeat = 12):
    for j in range(1,6):
        for x in itertools.combinations(range(201), j):
            k = np.zeros(285, int)
            k[0] = i[0]
            k[1] = i[1]
            k[2] = i[2]
            k[274] = i[3]
            k[275] = i[4]
            k[276] = i[5]
            k[277] = i[6]
            k[279] = i[7]
            k[280] = i[8]
            k[282] = i[9]
            k[283] = i[10]
            k[284] = i[11]
            for p in x:
                k[p] = 1
            X = np.vstack([X, k])
            y = np.vstack([y, 0])

np.savetxt("trainX2.csv", X, fmt = '%d', delimiter = ",")
np.savetxt("trainy2.csv", y, fmt = '%d', delimiter = ',')
'''