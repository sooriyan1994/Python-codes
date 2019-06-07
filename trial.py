import numpy as np
import random
from dist_bw_pts import distance,new_point,border,coord_plot
import matplotlib.pyplot as plt

##d = int(raw_input("Enter the diameter of the fibre (in microns): "))
d = 4
A_f = np.pi * d**2 /4
##a = int(raw_input("Side of the square area to be filled: "))
a = 10
A = a**2

##V_f = float(raw_input("Preferred Volume fraction: "))
V_f = 0.45
n = int(V_f * A/A_f)
print n

border = border(a)

mag = 3*d/2
coord = [[0,0]]

for i in range(n):
    k = 1
    while (k > 0):
        np = new_point(mag,coord[i])
        if (-a/2) <= np[0] <= (a/2) and (-a/2) <= np[1] <= (a/2):
            for l in range(len(border)):
                if distance(np,border[l]) < mag:
                    break
            else:
                for j in range(i):
                    print j
                    if distance(np,coord[j]) < mag:
                        break
                else:
                    break
        else:
            continue
               
    coord.append(np)
    
print coord

##test = coord[random.randint(0,n)]
##dis = []
##for i in range(n):
##    dis = dis + [distance(test,coord[i])]
##print dis

coord_plot(border)
coord_plot(coord)
