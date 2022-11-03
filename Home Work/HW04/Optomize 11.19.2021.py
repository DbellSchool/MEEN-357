from numpy.lib.type_check import imag
from scipy.optimize import minimize_scalar
from math import sqrt

def f(x,a):

    return (x-a)**2

a =1.5


def goldserach(f,bounds, imax=20,tol = 1e-7):
    r = (sqrt(5)-1)/2
    d = r*(bounds[1]-bounds[0])

    x1 = bounds[0] +d
    x2 = bounds[1] -d

    f1 = f(x1)
    f2 = f(x2)

    for i in range (imax):
        if bounds[1] - bounds[0] <=tol:
            if (f(bounds[1]) > f(bounds[0])):
                return bounds[1]
            else:
                return bounds[0]

        else:
            if(f1 > f2):
                bounds[0] = x2
                x2 = x1
                f2 = f1
                bounds[0] = bounds[0]+d
                f1 = f(x1)
            else:
                bounds[1] = x1
                x1 = x2
                f1=f2
                x2 = bounds[1] -d
                f2 = f(x2)


res = minimize_scalar(f,bounds=(0,1), args = a, method="bounded")

xstar = res.x

print(xstar)

b = []
res2 = goldserach(f,)
