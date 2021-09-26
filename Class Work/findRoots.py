from numpy import cbrt,finfo,sign
import sys

from numpy.lib.function_base import gradient
h= cbrt(finfo(float).eps)

def NR(f,x0,df=None,tol = 1.e-9):
    from numpy import cbrt,finfo,sign
    import sys
    def gradient(x):
        return (f(x+h)-f(x-h))/(2*h)
    fi = f(x0)
    if df == None:  
        dfc = gradient(x0)
    else:
        dfc = df(x0)
    xn = xc - fc/dfc
    fn = f(xn)
    while (abs((xn-xc)/xn)>tol):
        xc = xn
        fc = fn
        if df == None:  
            dfc = gradient(x0)
        else:
            dfc = df(x0)
        xn = xc - fc/dfc
        fn = f(xn)
    return xn
def (NRE)