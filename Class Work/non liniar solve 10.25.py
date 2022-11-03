import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.optimize import root_scalar

def ODE(X,y,L,h,Ta):
    T = y[0]
    Z =y[1]
    dtdx = X
    dzdx = h*(T*Ta)
    return np.array([dtdx,dzdx])

T0 = 40
Tl = 200 
L = 10
Ta = 20
h = 5e-9

fun1 = lambda x,y: ode(x,y,L,h,Ta)
tspan = np.array([0,L])



def residual(f,tspan,Z0, Tl):
    y0 = np.array([T0,Z0])
    sol = solve_ivp(f,tspan,y0)

    return Tl - sol.y[0,-1]

g = lambda Z0: residual(fun1,tspan,Z0,Tl)



# plt.plot(x1,y1,'-b')
# plt.plot(x2,y2,'-r')
# plt.plot(x3,y3,'-k')
# plt.xlabel('x')
# plt.ylabel('T')
# plt.grid('on')

# plt.show()