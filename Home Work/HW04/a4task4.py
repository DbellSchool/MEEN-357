
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import numpy as np
# solve ivt
# t = 0  to 2
# y(0) = 1 


f = lambda t, y: y*t**3-1.5*y # ODE

#A analytical
# see paper calculations
f0 = lambda t: np.exp(t**4/4-1.5*t)


#B Euleres methso h= 0.5 and 0.25
# Explicit Euler Method
def euler(f,h,y0 = 1):
    t = np.arange(0, 2, h) # sets range
    s = np.zeros(len(t)) # reates array to fill with y val
    s[0] = y0 # Initial Condition

    for i in range(0, len(t) - 1):
        s[i + 1] = s[i] + h*f(t[i], s[i])

    return t,s
h1 = 0.5 # step size
h2 = 0.25 # Step size

s=euler(f,h1)[1]
t= euler(f,h1)[0]


s2 = euler(f,h2)[1]
t2= euler(f,h2)[0]



#C
# midpoint method h =0.5

def mid(f,h,y0 = 1):
    t = np.arange(0, 2, h) # list of t values
    s0 = y0 # Initial Condition
    s = np.zeros(len(t))
    s[0] = s0
    for i in range(0, len(t)-1):
        #p = f[i]
        y = s[i] + f(t[i],s[i])*h/2
        s[i+1] = s[i] + f(t[i]+0.5*h,y) * h

    return t,s
h1 = 0.5 # Step size

s3=mid(f,h1)[1]
t3= mid(f,h1)[0]
t= mid(f,h1)[0]




#D fourth order RK  h = 0.5
def RK4(f,h,y0 = 1):
    t = np.arange(0, 2, h) # list of t values
    s = np.zeros(len(t))
    s[0] = y0 # initial condition
    for i in range(0, len(t)-1):
        #p = f[i]
        k1 = f(t[i],s[i])
        k2 = f(t[i]+h/2,s[i]+k1*h/2)
        k3 = f(t[i]+h/2,s[i]+ k2*h/2)
        k4 = f(t[i]+h,s[i]+k3*h)

        s[i+1] = s[i]+(k1+2*k2+2*k3+k4)/6*h

    return t,s
h1 = 0.5 # Step size

s4 = mid(f,h1)[1]
t4 = mid(f,h1)[0]
t4  = mid(f,h1)[0]

#Plot
plt.plot(t, s, 'ro--', label='euler [h=0.5]')
plt.plot(t2, s2, 'go--', label='euler [h=0.25]')
plt.plot(t3, s3, 'ko--', label='midpoint [h=0.25]')
plt.plot(t4, s4, 'yo--', label='RK4 [h=0.25]')
plt.plot(t, np.exp(t**4/4-1.5*t), 'b', label='Exact')
plt.title('ODE')
plt.xlabel('t')
plt.ylabel('f(t)')
plt.grid()
plt.legend()
plt.show()

