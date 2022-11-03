import numpy as np
import matplotlib.pyplot as plt

def f(T,a):
    y = a[0] + a[0]*T + a[0] *T**2

    return 1/y



def quadZ(x):
    n = len(x)
    Z = np.ones((n,3),dtype=float)
    Z[:,1] = x[:]
    Z[:,2] = x[:]**2
    return Z

def quadModel(x,a):
    y = a[0]+ a[1]*x + a[2]*x**2
    return y


def qubic(x,y):
    n = len(x)

    Z = quadZ(x)
    A = np.dot(np.transpose(Z),Z)

    b = np.dot(np.transpose(Z),y)
    param = np.linalg.solve(A,b)

    # plotting
    num = 100
    xmodel = np.linspace(x[0],x[n-1],num)
    ymodel = np.zeros(num)
    ymodel[:] = quadModel(xmodel[:],param)


    ##plot
    ax  = plt.subplot(1,1,1,)

    plt.tick_params(axis='both',which = 'major', labelsize = 12)
    plt.tick_params(axis='both',which = 'minor', labelsize = 10)
    l1, = ax.plot(x,y,'ko')
    l2, = ax.plot(xmodel,ymodel,'k-')
    plt.xlabel('x')
    plt.ylabel("y")
    plt.legend([l1,l2],["data","model"])
    plt.show()

    return param

T = np.array([10,20, 30, 40, 50, 60, 70])
u = np.array([1.308,1.005, 0.801, 0.656, 0.549 ,0.469, 0.406])
U = 1/u

coef = qubic(T,U)
print(coef)



