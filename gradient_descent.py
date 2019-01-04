def gradient_descent(X,y,theta, alpha, no_iters):
    import numpy as np
    from linear_reg_cost_fn import cost_fn
    m = len(y); 
    J_history = np.zeros([no_iters, 1]);

    for i in range(0,no_iters):
        H = X.dot(theta);
        slope = np.transpose(X).dot(H - y)/m
        theta = theta - alpha*slope
        J_history[i] = float(cost_fn(X,y,theta))
        
    return (theta,J_history)
