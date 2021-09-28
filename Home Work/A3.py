from math import cos, sin, factorial
from operator import xor
x=0

#Task 1
def bisection(y,L,R,tol = 9e-2,n=100):
    from numpy import sign 
    # look at initla inteval
    count = 0
    while (tol > maxEr):
        mid = (L + R)/2
        if (count >n):
            raise NameError("1 :algorithm terminated normally (due to error being sufficiently small)") 
        if f(R)*f(l) >= 0:
            raise NameError("2 : algorithm terminated due to invalidreturn value from function fun (e.g., NaN, Inf, empty bracket")
            
            
        # cechk curret poitn, 
        if f(mid) == 0.0:
            break
        elif f(mid)*f(R) < 0: 
            L = mid 
        elif f(mid)*f(L) < 0:
            R = mid
        
        tol = mid - (L + R)/2 < tol

        count += 1


# 1 :algorithm terminated normally (due to error being sufficiently small)
# 0 : algorithm terminated due to max iterations being reached-
# 1 : algorithm terminated due to invalid bracket specification (no root in bracket)-
# 2 : algorithm terminated due to invalidreturn value from function fun (e.g., NaN, Inf, empty bracket)

    return (xl+xr)/2.0, tol, n, flag

#Task 2
def falsepos(y,low,up,maxEr,minEr):

    return x,err,n,flag



#Task 3
def secant(y,low,up,maxEr,minEr):


    return x,err,n,flag







#Task 4
#Using yourPython functionsfrom Tasks 1-3, find allrootsfor eachofthe following functions on the range  −6≤𝑥≤6:
y=x*sin(x)+3*cos(x)- x
y=x*(sin(x)-x*cos(x))
y=(x**3-2**2+5*x-25)/40

# Task 5