#importing libraries for plotting and matrix operations
#import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt

#Opening the data file and reading data
with open('ex2data1.txt') as fl:
    V = []
    for line in fl:
        line = line.translate(None, '\n')
        V.append(line.split(',')) #removing commas and storing the data

V = np.array(V, dtype = float)

#getting X and y from the data
X = V[:,range(2)].reshape((len(V),1)) #.hstack is to add columns, similarly .vstack for rows
y = V[:,2].reshape((len(V),1))

#visualising the two features
pos = np.where(y == 1)
neg = np.where(y == 0)
plt.plot(X[pos,0], X[pos,1], 'yo', X[neg,0], X[neg,1], 'rx')
plt.xlabel('Exam 1 score')
plt.ylabel('Exam 2 score')
plt.legend('Admitted', ' Not Admitted')

#adding the bias term to the data
X = np.vstack(([np.ones(len(V)),X])).transpose()

#Initializing theta
theta = np.zeros([len(V),1],dtype= float)

