with open('ex1data1.txt') as fl:
    i=0;
    V = []
    for line in fl:
        line = line.translate(None, '\n')
        V.append(line.split(','))
        i+= 1

import matplotlib.pyplot as plt
plt.plot(V[:,0],V[:,1])
