from sigmoid import sigmoid
import numpy as np

def cost_fn(theta, X, y):

    m = len(y)
    J = 0;  #Cost Function      
    
    H = sigmoid(X.dot(theta)) #Hypothesis
    
    J = sum(-(np.log(H)*(y) + np.log(1-H)*(1-y)))/m
    print J
    return float(J)


def gradient_descent(theta, X, y):

    H = sigmoid(X.dot(theta))
    m = len(y)
    
    #Gradient Descent
    slope = np.transpose(X).dot(H - y)/m
    return slope
