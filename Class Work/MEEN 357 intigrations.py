import numpy as np
from scipy.integrate import quad, trapz, simps

def myfun(x):
    return x**2

x = np.linspace(0,2*np.pi,20)

int1 = simps(myfun(x),x)
int2 = trapz(myfun(x),x)
#quad()
#int3 = quad(myfun(x),x)


