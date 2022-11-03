import numpy as np 
from gaussElim2 import solve
from numpy.linalg import inv, det
from copy import deepcopy

A = np.array([[3,2,1],[4,5,2],[1,3,7]])
B = np.array([[1,0,0],[0,1,0],[0,0,1]])

Aorg = A.copy()

x = solve(A,B)

print(A)
print(x)
print(inv(Aorg))

print(A[0,0]*A[1,1]*A[2,2])
print(det(Aorg))
