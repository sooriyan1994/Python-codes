def sigmoid(z)

import numpy as np

g = np.zeros(z.shape)
z = np.array(z, dtype = float)

g = 1/(1+np.exp(-z))

return g
