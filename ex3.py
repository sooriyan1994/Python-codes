import scipy.io
mat = scipy.io.loadmat('ex3data1.mat')
X = mat['X']
y = mat['y']
mat_theta = scipy.io.loadmat('ex3weights.mat')
theta1 = mat_theta['Theta1']
theta2 = mat_theta['Theta2']
#Some code to display the array of data visually

