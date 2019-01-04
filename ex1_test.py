#importing libraries for plotting and matrix operations
#import matplotlib.pyplot as plt
import numpy as np
from linear_reg_cost_fn import cost_fn
from gradient_descent import gradient_descent

#Opening the data file and reading data
with open('ex1data1.txt') as fl:
    i=0;
    V = []
    for line in fl:
        line = line.translate(None, '\n')
        V.append(line.split(',')) #removing commas and storing the data
        i+= 1

V = np.array(V, dtype = float)

#Plotting the training data
#plt.plot(V[:,0],V[:,1],'rx')
#plt.xlabel('Population in 10000s')
#plt.ylabel('Price in 10000$')


#adding bias column to X
X = np.vstack(([np.ones(len(V)),V[:,0]])).transpose() #.hstack is to add columns, similarly .vstack for rows
y = V[:,1].reshape((len(V),1))

#defining the other parameters
no_iters = int(raw_input('Enter the number of iterations (1000~2000) : '))
alpha = float(raw_input('Enter the learning rate (0.001~3) : '))

#Initializing theta
theta = np.zeros([2,1],dtype= float)
J = float(cost_fn(X,y,theta))

#GRADIENT DESCENT
(theta, J_history) = gradient_descent(X, y, theta, alpha, no_iters)

#plotting the results
#plt.plot(X(:,2), X*theta, '-')
#plt.legend('Training data', 'Linear regression')

#Visualising J
#theta0 = np.linspace(-10, 10, 100)
#theta1 = np.linspace(-1, 4, 100)

#Initialize J_vals to a matrix of zeros
#J_vals = np.zeros(len(theta0), len(theta1))

#Generating the cost function values at the mesh points
#for i in range(0,theta0):
#    for j in range(0,theta1):
#        t = [theta0[i], theta1[j]]
#        J_vals = cost_fn(X, y, t)

#CONTOUR PLOT TO VISUALIZE J
#plt.contour(theta0, theta1, J_vals)
#plt.xlabel('\theta_0')
#plt.ylabel('\theta_1')
