def mapFeature(X1, X2):
    import numpy as np
    degree = int(raw_input('Enter the polynomial degree : '))
    n = np.ones([len(X1),1])
    for i in range(1, degree+1) :
                for j in range(i+1):
                    n = np.hstack((n,(X1**(i-j)*X2**j).reshape([len(X1),1])))

    return n
            
            
