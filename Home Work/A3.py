from math import cos, sin, factorial
from operator import xor
import matplotlib.pyplot as plt
from numpy.core.function_base import linspace
x=0

#Task 1
def bisection(f,L,R,toll = 9e-2,n=100):
    LR =L
    RR = R
    from numpy import sign 
    # look at initla inteval
    flag = -1
    tol = toll+1
    count = 0
    while (tol > toll):
        print(count)
        
        if (count > n):
            raise NameError("0 : algorithm terminated due to max iterations being reached-")
            flag = 0
            #return
        if f(R)*f(L) >= 0:
            raise NameError("1 : algorithm terminated due to invalidreturn value from function fun (e.g., NaN, Inf, empty bracket")
            flag = 1
            #return
        
        mid = (L + R)/2   
            
        # cechk curret poitn, 
        if f(mid) == 0.0:
            break
        elif f(mid)*f(R) < 0: 
            L = mid 
        elif f(mid)*f(L) < 0:
            R = mid
        
        
        tol = mid - (L + R)/2

        count += 1
    #try : 
    #    valtoTreturn = (l+R)/2.0, tol, n , flag
    #except:
    #    raise NameError("2 : algorithm terminated due to invalidreturn value from function fun (e.g., NaN, Inf, empty bracket)")


# -1 :algorithm terminated normally (due to error being sufficiently small)
# 0 : algorithm terminated due to max iterations being reached-
# 1 : algorithm terminated due to invalid bracket specification (no root in bracket)-
# 2 : algorithm terminated due to invalidreturn value from function fun (e.g., NaN, Inf, empty bracket)
    print((L+R)/2.0)
    
#Plots values for testing
    x =linspace(LR,RR,abs(LR-RR) *8)
    y = []
    for i in x:
        y.append(f(i))

    plt.plot(x,y, '-b')
    plt.show()
# end testign section

    return (L+R)/2.0, tol, n, flag

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





bisection(y1,-30,30)




# Task 5