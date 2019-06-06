import math
import random
def distance(X1,Y1):
    if isinstance(X1,list) and isinstance(Y1, list):
        dis = math.sqrt((X1[0]-Y1[0])**2+(X1[1]-Y1[1])**2)
    else:
        print('ERROR. The inputs have to be of type "list"')
    return round(dis,4)

def new_point(mag, cp):
    n1 = round(random.uniform(-1,1),4)
    n2 = round(math.sqrt(1 - n1**2),4)
    x = cp[0] + (mag*n1)
    y = cp[1] + (mag*n2)
    np = [round(x,4),round(y,4)]
    return np
