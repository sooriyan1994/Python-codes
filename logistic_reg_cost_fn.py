def cost_fn(theta, X, y):
    m = len(y)
    J = 0;
    grad = np.zeros(theta.shape)

    H = sigmoid(
