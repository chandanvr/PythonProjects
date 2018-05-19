import numpy as np
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import os as os

X=[]
Y=[]

script_dir = os.path.dirname(__file__)
abs_file_path = script_dir + "/data_2d.csv" 

for line in open(abs_file_path):
    x1,x2,y= line.split(',')
    X.append([1, float(x1),float(x2)])
    Y.append(float(y))

    X = np.array(X)
    Y = np.array(Y)

    fig= plt.figure()
    ax = fig.add_subplot(111,projection='3d')
    ax.scatter(X[:,0],X[:,1],Y)
    plt.show()
