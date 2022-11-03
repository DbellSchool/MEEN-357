import numpy as np 
import matplotlib.pyplot as plt

p = [1, 2, 3, 4, 5, 6, 7]
color = ["-r","-c","-b","-y","-g","-k","-m"]

x = 2 

def RTK4 (f,tspan,y0,N, p=1 ):
    n = len(y0)
    y = np.zeros((n,N+1),dtype=float)
    y[:,0] = y0
    x = np.linspace(tspan[0],tspan[1],N+1)
    h = (tspan[1]-tspan[0])/N
    for i in range(N):
        xi = x[i]
        yi = y[:,i]
        k1 = f(xi,yi)
        k2 = f(xi +1/2*h,yi + 1/2*k1*h)
        k3 = f(xi +1/2*h,yi + 1/2*k2*h)
        k4 = f(xi + h, yi+k3*h)
        y[:,i+1] = yi +1/6*(k1+1/3*k2+1/3*k3+1/6*k4)*h
    return x,y

def ODE(x,y):
    dy1dt = y[1]
    dy2dt = -0.5*y[1] - 7*y[0]
    return np.array([dy1dt, dy2dt])

y0 = 4
yy0 = 0
y0 = [y0,yy0]

# solve
h = 0.5**20
span = np.array([2-h,2+h])
N = int((span[1]-span[0])/h)
True_XY_atX2 = RTK4(ODE,span,y0,N)


print("Aprx Slope is:")
for i in range(len(p)):
    
    h = 0.5**p[i]
    span = np.array([2-h,2+h])
    N = int((span[1]-span[0])/h)
    x,y = RTK4(ODE,span,y0,N)
    #print("Avg Slope P",p[i],"is:",sum(y[1,:])/len(y[1:]))
    print("True error P= ",p[i],"is", True_XY_atX2[1][0,1]- y[0,1] )

    string = "P ="+ str(p[i]) + "  | h ="+str(h) 
    plt.plot(x,y[0,:],color[i],label =string)
    
plt.legend()
plt.show()

