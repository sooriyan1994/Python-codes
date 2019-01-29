from sigmoid import sigmoid
import numpy as np

def cost_fn(theta, X, y):

    m = len(y)
    J = 0;  #Cost Function      
    
    H = sigmoid(X.dot(theta)) #Hypothesis
    J = np.sum(-np.log(H)*(y) - np.log(1-H)*(1-y))/m
    return J


def gradient_descent(theta, X, y):

    H = sigmoid(X.dot(theta))
    m = len(y)
    
    #Gradient Descent
    slope = (np.transpose(X).dot(H - y))/m
    return slope

def predict(theta, X, y):

    m = len(y)
    p = np.zeros([m,1])
    H = sigmoid(X.dot(theta))
    prediction = np.zeros(len(y))

    p[np.where(H>=0.5)] = 1

    return p

def cost_fn_reg(theta, X, y, lamda):

    m = len(y)
    J = 0

    H = np.array(sigmoid(X.dot(theta))).reshape(len(X),1)
    J = np.sum(-np.log(H)*(y) - np.log(1-H)*(1-y))/m + np.sum(theta**2)*(lamda/2*m)
    return J

def gradient_descent_reg(theta, X, y, lamda):

    H = sigmoid(X.dot(theta))
    m = len(y)
    
    #Gradient Descent
    slope = (np.transpose(X).dot(H - y) + lamda*theta)/m
    return slope
