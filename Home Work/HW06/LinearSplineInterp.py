import numpy as np 
import matplotlib.pyplot as plt
from numpy.core.function_base import linspace

def LinearSplineInterp(x,xnew,a): # graphs based on initla locaiotn of data
    n = len(xnew)
    N = len(x)
    ynew = []
    for j in range(n):
        xindex = 0 
        for i in range(N-1):
            if (xnew[j] >= x[i] and xnew[j] <= x[i+1]):
                xindex = i
                break 
            elif(xnew[j] < x[0]):
                xindex = 0
            elif(xnew[j] < x[0]):
                xindex = -1
        ynew.append( a[xindex][1]*xnew[j]+a[xindex][0]) 
    return ynew

