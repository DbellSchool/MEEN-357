def myFun(x):

    return x**2.0

def forwardDiff(f,x,h):
    return (f(x+h)-f(x))/h

def backwordDef(f,x,h):
    return (f(x)-f(x-h))/h

def CentralDiff(f,x,h):
    return (f(x+h)- f(x-h))/(2.0*h)

import numpy as np
import matplotlib as plt

N= 12
h= 0.1
x= 1.0

hn = np.zeros((N,1), dtype=float)
error = np.zeros((N,1),dtype=float)
dft = 2.0 * x

for i in range (N):
    hn[i] = h/10**i
    dfa = forwardDiff(myFun,x,hn[i])
    error[i] = abs(dft-dfa)

plt.loglog(hn,error,'o-b')
plt.xlabel('Step Size')
plt.ylabel("Trues erro")
plt.show()
