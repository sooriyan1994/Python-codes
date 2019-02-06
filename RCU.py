#RCU works

import numpy as np
import matplotlib.pyplot as plt

rho_m = raw_input('Enter the elastic modulus of the material used : ')
a = raw_input('Enter the edge length of Hexagonal Unit Cell : ')
t = float(raw_input('Thickness of the hexagonal cell : '))
S = np.sqrt(3) * a  #CELL SIZE
rho_c = rho_m * (8 * t_c) / (3 * S)
print 'Density of the sandwich core ',rho_c

#t_j = float(raw_input('Thickness of the joints of the hexagonal cell : '))

Cell_X = np.linspace(0,3*a,51)
Cell_y = np.linspace(-0.5*S,0.5*S,51)
cell_mesh_x, cell_mesh_y = np.meshgrid(Cell_X,Cell_Y)

cd_O = np.array([0, 0])
OA = np.array([0,a/2],[0,0])
cd_A = np.array([a/2, 0])
cd_D = np.array([5*a/2, 0])
cd_X = np.array([3*a, 0])
cd_B = np.array([a, np.sqrt(3)*a/2])
cd_F = np.array([a, -np.sqrt(3)*a/2])
cd_C = np.array([2*a, np.sqrt(3)*a/2])
cd_E = np.array([2*a, -np.sqrt(3)*a/2])


coord = ([0,0],[a/2,0],[a,np.sqrt(3)*a/2],[2*a,np.sqrt(3)*a/2],[5*a/2,0],[3*a,0],[a,-np.sqrt(3)*a/2],[2*a,-np.sqrt(3)*a/2])
coord = np.array(coord)

for i in range(len(coord)):
    plt.plot(coord[i,0],coord[i,1],'go')
