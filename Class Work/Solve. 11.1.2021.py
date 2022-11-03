##from 
import numpy as np
import matplotlib.pyplot as plt 


a = 0.0 
b = 5.0
alpha  =1.0
beta = 0.0
case = 2
n = 20 

example = finiteDifference()

def f(x,y,yprim):
    return yprim - (1-0.2*x)*y

y0 - np.ones(N,dtype =float)
x,y, = example.solve(a,b,alpha,beta,case,y0,f)

plt.plot(x,y,'-k')
plt.xlabel('x')
plt.ylabel('T')
plt.grid('on')

plt.show()