import numpy as np
import random
from dist_bw_pts import distance,new_point
import matplotlib.pyplot as plt

##d = int(raw_input("Enter the diameter of the fibre (in microns): "))
d = 6
A_f = np.pi * d**2 /4
##A = int(raw_input("Area of the square to be filled: "))
A = 1600
##V_f = float(raw_input("Preferred Volume fraction: "))
V_f = 0.45
n = int(V_f * A/A_f)

mag = 3*d/2
coord = [[0,0]]
for i in range(n):
    k = 1
    while (k > 0):
        np = new_point(mag,coord[i])
        for j in range(i):
            if distance(np,coord[j]) < mag:
                continue
        break                
       
    coord.append(np)
    
print coord

test = coord[random.randint(0,n)]
dis = []
for i in range(n):
    dis = dis + [distance(test,coord[i])]
print dis

X = []; Y = [];
for i in range(n):
    X = X + [coord[i][0]]
    Y = Y + [coord[i][1]]

plt.plot(X,Y)
plt.show()
