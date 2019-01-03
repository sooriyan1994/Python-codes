def cost_fn(X,y,theta):
    import numpy as np
    m = len(y)
    J = 0

    H = X.dot(theta)
    J = sum(np.square(H - y))/(2*m)
    
    return J
