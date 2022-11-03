
import numpy as np


def gausselim(A,b):
    n = len(b)
    b[n-1] = b[n-1]/ U[n-1,n-1]
    for k in range(n-1):
        for i in range(k+1,n):
            if A[i,k] != 0.0:
                lamda = A[i,k]/ A[k,k]

                A[i,k] = 0.0 
                A [i,k+1:n] = A[i,k+1:n] - lamda*A[k,k+1:n]
                b[i] = b[i] - lamda * b[k]

    b[n-1] = b[n-1]/ A[n-1,n-1]
    for i in range( n-2,-1,-1):
        b[i] =( b[i] - np.dot(A[i,i+1:n],b[i+1:n]))/ A[i,i]

    return b

def backSub(U,b):
    n = len(b)
    b[n-1] = b[n-1]/ U[n-1,n-1]
    for i in range( n-2,-1,-1):
        b[i] =( b[i] - np.dot(U[i,i+1:n],b[i+1:n]))/ U[i,i]


