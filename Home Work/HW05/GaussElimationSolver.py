## Task 4 
import numpy as np


def GaussElimationSolver(A,b):
    n = len(b)
    for k in range(n-1):
        for i in range(k+1,n):
            #print(A[i,k])
            if A[i,k] != 0.0 or A[i,k] != 0:
                lamda = A[i,k]/ A[k,k] # gets val to mult across
                A[i,k] = 0.0 #  sets elem to 0
                A[i,k+1:n] = A[i,k+1:n] - lamda*A[k,k+1:n]
                b[i] = b[i] - lamda * b[k]


    b[n-1] = b[n-1]/ A[n-1,n-1]
    #print( b[n-1]/ A[n-1,n-1])
    for k in range( n-2,-1,-1):
        b[k] =( b[k] - np.dot(A[k,k+1:n],b[k+1:n]))/ A[k,k]

    return b


#A = np.array([[0,1,-1],[1,0,0],[0,0,1]],dtype=float)
#B = np.array([0,1,1],dtype=float)

#T = np.linalg.solve(A, B) 
#print(T)

#g =GaussElimationSolver(A,B)
#print(g)