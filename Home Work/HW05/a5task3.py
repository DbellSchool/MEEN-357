import numpy as np
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import transpose
from numpy.lib.function_base import rot90
from numpy.lib.nanfunctions import _remove_nan_1d

h = (1-0.5)/9 # Finds h val

# all rn terms
r0 = 0.5 
r1 = 0.5+h*1
r2 = 0.5+h*2
r3 = 0.5+h*3
r4 = 0.5+h*4
r5 = 0.5+h*5
r6 = 0.5+h*6
r7 = 0.5+h*7
r8 = 0.5+h*8
r9 = 0.5+h*9
r = [r0,r1,r2,r3,r4,r5,r6,r7,r8, r9]

# equation matric 9 terms plus 2 end conditions (11x11)
A = np.array([[0,0.5,0,0,0,0,0,0,0,0,0],
                [2*r0-h,-4*r0,2*r0+h,0,0,0,0,0,0,0,0],
                [0,2*r1-h,-4*r1,2*r1+h,0,0,0,0,0,0,0],
                [0,0,2*r2-h,-4*r2,2*r2+h,0,0,0,0,0,0],
                [0,0,0,2*r3-h,-4*r3,2*r3+h,0,0,0,0,0],
                [0,0,0,0,2*r4-h,-4*r4,2*r4+h,0,0,0,0],
                [0,0,0,0,0,2*r5-h,-4*r5,2*r5+h,0,0,0],
                [0,0,0,0,0,0,2*r6-h,-4*r6,2*r6+h,0,0],
                [0,0,0,0,0,0,0,2*r7-h,-4*r7,2*r7+h,0],
                [0,0,0,0,0,0,0,0,2*r8-h,-4*r8,2*r8+h],
                [0,1,0,0,0,0,0,0,000000,1.000,000000]])

b = np.array([0,0,0,0,0,0,0,0,0,000,200]) # end conditions


def Tru(r,a):  # true value equaitons
    y = 200.*(1-np.log(r/a)/np.log(0.5))
    return y


YTrial = np.linalg.solve(A, transpose(b)) #calculates y val   y-1 to yn
x = np.linspace(0.5,1 , 10) # gets daa points for true val calculaiton
a =1

# plots figs
plt.plot(x,Tru(x,a),"o-b", label='True')
plt.plot(r,YTrial[1:],"o-k",label='BPV')
plt.legend(loc='best')
plt.xlabel('x')
plt.xlabel('y')
plt.grid()
plt.show()