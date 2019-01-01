def gradient_descent(X,y,theta, alpha, no_iters):
    import numpy as np
    from linear_reg_cost_fn import cost_fn
    m = length(y); 
    J_history = np.zeroes(num_iters, 1);

    H = X * theta;

    for i in range(0,no_iters):
        for j in range(0,len(theta)):
            slope = sum(H - y) * X[j]
            theta[j] = theta[j] - alpha*slope

        J_history[i] = cost_fn(X,y,theta)

    return J_history
