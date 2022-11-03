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



# initial variabels
x = np.array([3.0, 4.5, 7.0, 9.0])
fx = np.array([2.5, 1.0, 2.5, 0.5])
a = LinearSpline(x,fx)
xnew = np.linspace(3.0, 9.0, 100)



ynew = LinearSplineInterp(x,xnew,a)


plt.plot(xnew,ynew,'bo') # creates and displays graphs
plt.plot(x ,fx,'ro')
plt.plot(x ,fx,'b-')
plt.show()