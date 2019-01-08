def feature(X):
    import numpy as np
    mu = np.mean(X, axis=0)
    sigma = np.std(X, axis=0)

    X = (X - mu)/sigma

    return (X, mu, sigma)
