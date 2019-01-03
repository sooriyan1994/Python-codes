def gradient_descent(X,y,theta, alpha, no_iters):
    import numpy as np
    from linear_reg_cost_fn import cost_fn
    m = len(y); 
    J_history = np.zeros([no_iters, 1]);

    H = X.dot(theta);

    for i in range(0,no_iters):
        for j in range(0,len(theta)):
            slope = float((sum(H - y)/m)) * X[j]
        print slope
        theta = theta - alpha*slope
        print theta
        J_history[i] = float(cost_fn(X,y,theta))
        
    return (theta,J_history)
