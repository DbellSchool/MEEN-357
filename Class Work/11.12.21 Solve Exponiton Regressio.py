import numpy as np
from numpy.core.function_base import linspace

import numpy.linalg as la
import matplotlib.pyplot as plt



def Lin(x):
    n = len(x)
    Z = np.ones((n,2),dtype=float)
    Z[:,1] = x
    return Z

def linMod(a,x):
    y = a[0]+ a[1]*x
    return y

def quadz(x):
    n = len(x)
    Z = np.ones((n,3),dtype=float)
    Z[:,1] = x
    Z[:,2] = X**2
    return Z

def quadMod(a,x):
    y = a[0]+ a[1]*x+ a[2]*x**2
    return y

XData = np.array([1994,1995,1996,1997,1998,1999,2000])
YData = np.array([356.8,358.2,360.3,361.8,364,365.7,366.7])

Z = Lin(XData)
b = YData

a = la.solve(Z.T@Z,Z.T@b)

x = np.linspace(1994,2000,100)
y = linMod(a,x)

plt.plot(XData,YData,'o-k')
plt.plot(x,y, '-b')
plt.legend(["data", " intrip"])
plt.show()