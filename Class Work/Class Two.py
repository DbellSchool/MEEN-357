# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 11:38:41 2021

@author: ripti
"""

def matrix():
    import numpy as np
    from numpy.linalg import solve, inv
    
    
    A = np.array([[1,2,3],[1,3,5],[1,4,8]],dtype = float)
    b = np.array([-1,-2,-3],dtype = float)
    
    x = solve(A,b)
    #Print('x = {:f}'.format(x))"
    
    
    return 

def plot ():
    import numpy as np
    import numpy.linalg as la
    
    A = np.array([[1,2,3],[1,3,5],[1,4,8]],dtype = float)
    b = np.array([-1,-2,-3],dtype = float)
    print(la.solve(A,b))
    print("\n\n")
    print(la.inv(A))
    
    return


def d2Plot():

    from numpy import linspace, sin, cos
    from math import pi 
    import matplotlib.pyplot as plt
    
    x = linspace(0,pi,50)
    # Arange is a list, Linspace is a vector
    
    
    
    plt.plot(x,cos(x), '^--b')
    plt.plot(x,sin(x), 'o-r')
    plt.xlabel("x")
    plt.ylabel('values')
    plt.title("Trig Functions")
    plt.legend(['cosin','sin'], loc = "lower left")
    plt.savefig("Triplot.jpg", format = "jpg")
    plt.show()

    print("\n\n")
    
    
    return

d2Plot()  
#InclassFun()

#plot()

#matrix()
