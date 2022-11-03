import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def ODE(X,y,L,h,Ta):
    T = y[0]
    Z =y[1]
    dtdx = X
    dzdx = h*(T*Ta)
    return np.array([dtdx,dzdx])

T0 = 40
Tl = 200 
L = 1
Ta = 20
h =0.01
tspan = np.array([0,L])
fun1 = lambda x,y: ODE(x,y,L,h,Ta)

y0 = np.array([T0,0])
sol1 = solve_ivp(fun1,tspan,y0)
x1= sol1.t
y1 = sol1.y[0,:]

fun2 = lambda x,y: ODE(x,y,L,h,0)
y0 = np.array([0,1])
sol2 = solve_ivp(fun2,tspan,y0)
x2= sol2.t
y2 = sol2.y[0,:]

c2 = (Tl-y1[-1])/y2[-1]

y0 = np.array([T0,c2])
sol3 = solve_ivp(fun1,tspan,y0)
x3= sol3.t
y3 = sol3.y[0,:]

plt.plot(x1,y1,'-b')
plt.plot(x2,y2,'-r')
plt.plot(x3,y3,'-k')
plt.xlabel('x')
plt.ylabel('T')
plt.grid('on')

plt.show()