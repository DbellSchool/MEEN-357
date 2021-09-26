from findRoots import NR

def Func(x):
    
    return x**2.0-x-2.0

x0 = NR(Func,10,1.0e-7)

print(x0)