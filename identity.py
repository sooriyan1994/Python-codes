def zeroes(n):
    "Returns a matrix of zeroes of size n*n"
    A=[];
    for i in range(n):
        A.append([0]*n);
    return A

def identity(n):
    "Returns an identity matrix of size n*n"
    A = zeroes(n);
    
    for i in range(n):
        for j in range(n):
            if i == j:
                A[i][j] = 1;
            
    return A

