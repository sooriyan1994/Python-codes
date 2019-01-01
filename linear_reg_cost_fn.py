def cost_fn(X,y,theta):
    import numpy as np
    m = length(y)
    J = 0

    H = X*theta
    J = sum(H - y)/(2*m)
    return J
