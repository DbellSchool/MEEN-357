from math import cos, sin, factorial, erf
from operator import xor
from os import error
import matplotlib.pyplot as plt
from numpy.core.function_base import linspace
from scipy.optimize import root_scalar # for finsing zero 
import numpy as np
x=0


#Task 1
def bisection(f,L,R,toll = 0.001,n= 100):
    flag = -1
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
    tol = toll*2
    count = 0
    a = True
    while a == True:
        #print(count)
        mid = (L + R)/2 
        #if mid == "null" or mid == "Nan" or mid = "Inf", or mid = null:
        #    l
            #return mid,erf(f(mid)) ,count, flag

        if (count > n):
            flag = 0 #raise Exception("0 : algorithm terminated due to max iterations being reached-")
            print("Exit with:",flag)
            return
        if np.sign(f(L)) == np.sign(f(R)):
            flag = 1 #raise Exception("1 : algorithm terminated due to invalid bracket specification (no root in bracket)")
            print("Exit with:",flag)
            return

        if abs(f(mid)) < tol:
            #print("-1 :algorithm terminated normally (due to error being sufficiently small)")

            return mid,erf(f(mid)) ,count, flag

        elif f(mid)*f(R) < 0: 
            L = mid 
            
        elif f(mid)*f(L) < 0:
            R = mid
        

        count += 1

# -1 :algorithm terminated normally (due to error being sufficiently small)
# 0 : algorithm terminated due to max iterations being reached-
# 1 : algorithm terminated due to invalid bracket specification (no root in bracket)-
# 2 : algorithm terminated due to invalidreturn value from function fun (e.g., NaN, Inf, empty bracket)
        #print((L+R)/2.0)

#Task 2
def falsepos(f,L,R,Err= 0.0001,N=100):
    if callable(f) == False:
        raise TypeError("0 : algorithm terminated due to max iterations being reached-")
    c =1
    print(c,N)
    
    a = True
    while a:
        if (c > N):
            flag = 0 #raise Exception("0 : algorithm terminated due to max iterations being reached-")
            print("Exit with:",flag)
            return
        m = L - (R-L) * f(L)/( f(R) - f(L) )
        

        if f(L) * f(m) < 0:
            R = m
        else:
            L = m

        c = c + 1
        print(m)
        if abs(f(m)) > Err:
            return m, erf(f(m)),c, -1


    return 

# def falsepos(y,low,up,maxEr,minEr):

#     return x,err,n, flag



#Task 3

def secant(f,a,b,tol = 0.00002,N=100):
    if callable(f) == False:
        raise TypeError("0 : algorithm terminated due to max iterations being reached-")

    if f(a)*f(b) >= 0:
        print("Exit Flag:",1)
        return None
    #a_n = a
    #b_n = b
    for n in range(1,N+1):
        m = a - f(a)*(b - a)/(f(b) - f(a))
        print(f(m))
        if f(a)*f(m) < 0:
            b = m
        elif f(b)*f(m) < 0:
            a = m
        if abs(f(m)) < tol :
            
            return m, erf(f(m)), n, -1

    print("Exit with flag",0)    
    return 
#def secant(y,low,up,maxEr,minEr):


#    return x,err,n,flag

#Plots values for testing
def plotF(f,LR,RR):
    x =linspace(LR,RR,abs(LR-RR) *8)
    y = []
    for i in x:
        y.append(f(i))

    plt.plot(x,y, '-b')
    plt.plot(x,np.zeros(len(x)),'-k')
    plt.show()







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


#plotF(y2,-10,10)
#plotF(y3,-10,10)

#print("the zero is at",bisection(y1,1,3, n=10)) # works
Y1_0 = []
Y2_0 = []
Y3_0 = []
for i in range(-6,6):
     #print(i)
     try:
         #print("the zero is at",bisection(y1,i,i+1, n=10))
         V1 = bisection(y1,i,i+1,n=10)[0]
         print(V1)
         #print(V1)    
         Y1_0.append(V1)
     except:
         pass
print(Y1_0)

for i in range(-6,6,2):
     #print(i)
    try:
        V2 = bisection(y2,i,i+2)[0]
        Y2_0.append(V2)
    except Exception:
        pass

    
        
for i in range(-6,6,11):

    try:
        V3 = bisection(y3,i,i+11)[0]
        Y3_0.append(V3)
    except:
        pass


print("\n\nTask 4\nUsign Bisect metion with bound for Y1 in incremetn of 1, Y2 in incremetns of 2 and Y3 in increments of 11. from -6-6")
print("Y1",Y1_0)
print("Y2",Y2_0)
print("Y3",Y3_0)


plotF(y1,-10,10)
print(secant(y1,1,4))

print(root_scalar(y1, method = 'bisect', bracket = [1,4]))



