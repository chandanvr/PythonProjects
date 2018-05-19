import numpy as np
import matplotlib.pyplot as plt
import os

X=[]
Y=[]
for line in open('E:\Git\Repositories\PythonProjects\data_1d.csv'):
    x,y = line.split(',')
    X.append(float(x))
    Y.append(float(y))

X = np.array(X)
Y = np.array(Y)

plt.scatter(X,Y)
plt.show()
