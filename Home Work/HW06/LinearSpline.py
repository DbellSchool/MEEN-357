import numpy as np 
import matplotlib.pyplot as plt
from numpy.core.function_base import linspace


def LinearSpline(x,y): # gets coeficiona for each linear spline
    n = len(x)
    coef = []
    for i in range(n-1):
        m = (y[i+1]-y[i])/(x[i+1]-x[i])
        
        b = y[i] - m*x[i]
        coef.append ([b,m])
        print(coef)
        X = linspace(x[i],x[i+1],10)
    return(coef)

