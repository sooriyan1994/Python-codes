#importing libraries for plotting and matrix operations
#import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as op
from logistic_reg_cost_fn import cost_fn, gradient_descent, predict, cost_fn_reg, gradient_descent_reg
from map_feature import mapFeature

#Opening the data file and reading data
with open('ex2data1.txt') as fl:
    V = []
    for line in fl:
        line = line.translate(None, '\n')
        V.append(line.split(',')) #removing commas and storing the data

V = np.array(V, dtype = float)

#getting X and y from the data
X = V[:,range(2)].reshape((len(V),2)) #.hstack is to add columns, similarly .vstack for rows
y = V[:,2].reshape((len(V),1))

#visualising the two features

#pos = np.where(y == 1)
#neg = np.where(y == 0)
#plt.plot(X[pos,0], X[pos,1], 'yo', X[neg,0], X[neg,1], 'rx')
#plt.xlabel('Exam 1 score')
#plt.ylabel('Exam 2 score')
#plt.legend('Admitted', ' Not Admitted')

#adding the bias term to the data
X = np.hstack((np.ones((len(V),1)),X))

#Initializing theta
init_theta = np.zeros(((len(X[2]),1)),dtype = float)

cost = cost_fn(init_theta, X, y)
slope = gradient_descent(init_theta, X, y)

#ADVANCED OPTIMISATION TECHNIQUE
opt_result = op.fmin_tnc(cost_fn, x0 = init_theta.flatten(), fprime = gradient_descent, args=(X, y.flatten()))
theta = np.array(opt_result[0])

####Plotting the decision boundary using the optimised theta is remaining)###

#GENERAL WAY TO USE ANY OPTIMIZER
#Using Newton-CG optimization technique
theta_opt = op.minimize(cost_fn, x0 = init_theta.flatten(), args = (X, y.flatten()),method = 'Newton-CG', jac = gradient_descent)

#PREDICTION ACCURACY
p = predict(theta, X, y)
pred = (p == y) * 1
Accuracy = np.mean(pred)*100
print 'Accuracy of the model is ',Accuracy



#USING REGULARIZATION

#Loading the data
with open('ex2data2.txt') as fl:
    V = []
    for line in fl:
        line = line.translate(None, '\n')
        V.append(line.split(',')) #removing commas and storing the data

V = np.array(V, dtype = float)

#getting X and y from the data
X_reg = V[:,range(2)].reshape((len(V),2)) #.hstack is to add columns, similarly .vstack for rows
y_reg = V[:,2].reshape((len(V),1))

#visualising the two features

#pos = np.where(y == 1)
#neg = np.where(y == 0)
#plt.plot(X[pos,0], X[pos,1], 'yo', X[neg,0], X[neg,1], 'rx')
#plt.xlabel('Microchip Test 1')
#plt.ylabel('Microchip Test 2')
#plt.legend('y=1', ' y=0')

X_reg = mapFeature(X_reg[:,0], X_reg[:,1]) #Create more features from each data point
init_theta = np.zeros(((len(X_reg[2]),1)),dtype = float) #initalising theta

lamda = int(raw_input('Enter the regularization parameter (lambda) (0-100): ')) #Regularization parameter
cost = cost_fn_reg(init_theta, X_reg, y_reg, lamda) 
grad = gradient_descent_reg(init_theta, X_reg, y_reg, lamda)
print cost

#ADVANCED OPTIMISATION TECHNIQUE - OPTIMIZER
opt_result = op.fmin_tnc(cost_fn_reg, x0 = init_theta.flatten(), fprime = gradient_descent_reg, args=(X_reg, y_reg.flatten(),lamda))
theta = np.array(opt_result[0])

####Plotting the decision boundary using the optimised theta is remaining)###

#PREDICTION ACCURACY
p = predict(theta, X_reg, y_reg)
pred = (p == y_reg) * 1
Accuracy = np.mean(pred)*100
print 'Accuracy of the model is ',Accuracy
