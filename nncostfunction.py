from sigmoid import sigmoid
import numpy as np
def nncostfn(theta1, theta2, X, y, lamda):
    input_layer_size = len(theta1[2])
    hidden_layer_size = len(theta2[2])
    no_labels = len(theta2)

    m = len(X)
    J = 0
    X = np.hstack((np.ones(m,1),X))
    H = sigmoid(X.dot(theta))

    J = np.sum(- np.log(H)*y - np.log(1-H)*(1-y))/m + (lamda/2*m)*np.sum(theta**2)
    return J
    
def gradient_descent(theta1, theta2, X, y, lamda):

    z_2 = X.dot(np.transpose(theta1))
    a_2 = sigmoid(z_2)
    a_2 = np.hstack(np.ones((len(X),1)),a_2)
    z_3 = a_2.dot(np.transpose(theta2))
    H = sigmoid(z_3)

    labels = np.array(range(1,11))
    for i in range(len(y)):
        y_label = np.zeros((1,10))
        y_label[np.where(labels == y[i])] = 1

    
        
        


    
