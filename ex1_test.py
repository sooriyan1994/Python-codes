#Opening the data file
import matplotlib.pyplot as plt
import numpy as np

with open('ex1data1.txt') as fl:
    i=0;
    V = []
    for line in fl:
        line = line.translate(None, '\n')
        V.append(line.split(','))
        i+= 1

X = np.hstack([np.ones(len(V)),V[:,0]])
y = V[:,1]
no_iters = raw_input('Enter the number of iterations: ')
alpha = raw_input('Enter the learning rate (0.001~3) : ')
theta = np.zeros(2,1)


plt.plot(V[:,0],V[:,1],'rx')
plt.xlabel('Population in 10000s')




plt.plot(X(:,2), X*theta, '-')
plt.legend('Training data', 'Linear regression')

   
    


