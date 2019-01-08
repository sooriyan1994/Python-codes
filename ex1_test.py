#importing libraries for plotting and matrix operations
#import matplotlib.pyplot as plt
import numpy as np
from linear_reg_cost_fn import cost_fn
from gradient_descent import gradient_descent
from feature_normalize import feature

#Opening the data file and reading data
with open('ex1data1.txt') as fl:
    V = []
    for line in fl:
        line = line.translate(None, '\n')
        V.append(line.split(',')) #removing commas and storing the data

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



#ADDITIONAL EXERCISES

with open('ex1data2.txt') as fl:
    V_multi = []
    for line in fl:
        line = line.translate(None, '\n')
        V_multi.append(line.split(',')) #removing commas and storing the data

V_multi = np.array(V_multi, dtype = float)

X_multi = V_multi[:,0:2]
y_multi = V_multi[:,2].reshape((len(V_multi),1))
m = len(y_multi)

(X_multi, mu, sigma) = feature(X_multi)
X_multi = np.hstack([np.ones(len(V_multi)).reshape((len(V_multi),1)),X_multi])

theta_multi = np.zeros([3,1],dtype= float)

no_iters_multi = 400
alpha_multi = 0.01
(theta_multi, J_history_multi) = gradient_descent(X_multi, y_multi, theta_multi, alpha_multi, no_iters_multi)
print theta_multi


#SOLVING WITH NORMAL EQUATIONS
X_norm = V_multi[:,0:2]
X_norm = np.hstack([np.ones(len(V_multi)).reshape((len(V_multi),1)),X_norm])
X_t = np.transpose(X_norm)
theta_norm = np.dot(np.dot(np.linalg.inv(np.dot(X_t, X_norm)),X_t),y_multi)

print theta_norm
