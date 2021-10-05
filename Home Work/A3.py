from math import cos, sin, factorial
from operator import xor
from os import error
import matplotlib.pyplot as plt
from numpy.core.function_base import linspace
import numpy as np
x=0


#Task 1
def bisection(f,L,R,toll = 9e-2,n=100):
    
    #if L>R: # makse sure directions of var is right
    #    tmep = L
    #    L=R
    #    R=temp

    LR =L
    RR = R
    if callable(f) == False:
        raise TypeError("0 : algorithm terminated due to max iterations being reached-")


    from numpy import sign 
    # look at initla inteval
    flag = -1
    tol = toll+1
    count = 0
    a = True
    while a == True:
        print(count)
        
        if (count > n):
            #raise Exception("0 : algorithm terminated due to max iterations being reached-")
            pass
        if np.sign(f(L)) == np.sign(f(R)):
            raise Exception("1 : algorithm terminated due to invalid bracket specification (no root in bracket)")


        mid = (L + R)/2   
            
        # cechk curret poitn, 
        if f(mid) < tol:
            print("-1 :algorithm terminated normally (due to error being sufficiently small)")
            return mid, n, flag

        elif f(mid)*f(R) < 0: 
            L = mid 

        elif f(mid)*f(L) < 0:
            R = mid
        

        count += 1
# -1 :algorithm terminated normally (due to error being sufficiently small)
# 0 : algorithm terminated due to max iterations being reached-
# 1 : algorithm terminated due to invalid bracket specification (no root in bracket)-
# 2 : algorithm terminated due to invalidreturn value from function fun (e.g., NaN, Inf, empty bracket)
        print((L+R)/2.0)
    
#Plots values for testing
def plotF(f,LR,RR):
    x =linspace(LR,RR,abs(LR-RR) *8)
    y = []
    for i in x:
        y.append(f(i))

    plt.plot(x,y, '-b')
    plt.plot(x,np.zeros(len(x)),'-k')
    plt.show()

#Task 2
def falsepos(y,low,up,maxEr,minEr):

    return x,err,n, flag



#Task 3
def secant(y,low,up,maxEr,minEr):


    return x,err,n,flag







#Task 4
#Using yourPython functionsfrom Tasks 1-3, find allrootsfor eachofthe following functions on the range  −6≤𝑥≤6:
y=x*sin(x)+3*cos(x)- x
y=x*(sin(x)-x*cos(x))
y=(x**3-2**2+5*x-25)/40

def y1(x):
    return x*sin(x)+3*cos(x)- x
def y2(x):
    return x*(sin(x)-x*cos(x)) 
def y3(x):
    return(x**3-2**2+5*x-25)/40

print(type('HI'))
c = 5



plotF(y1,-10,10)
#bisection(y1,-1,1)




# Task 5