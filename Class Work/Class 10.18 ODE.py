import numpy as np
from  scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from scipy.interpolate import PchipInterpolator as Pchip

def Example1():

    def ODE(t,y,m,c,k):

        dy2dt = -k/m*y[0] -c/m*y[1]
        dy1dt = y[1]

        return np.array([dy2dt,dy1dt])

    m = 20  #kg
    k = 10  #N/m
    c = 5   #N-s/m

    x0 = 0.02 # m
    v0 = 0    # m/s
    y0 = np.array([x0,v0])

    t0 = 0.0    #inital time
    tf = 120.0  #final time
    t_span = np.array([t0,tf])



    ode = lambda t,y: ODE(t,y,m,c,k)

    sol = solve_ivp(ode,t_span,y0, method = 'RK45')

    T=sol.t # time vector
    X = sol.y[0,:] # displacement solution vector
    V = sol.y[1,:] # velocity soution vector

    plt.subplot(2,1,1)
    plt.plot(T,X,'x-b')
    plt.xlabel("Time [s]")
    plt.ylabel("Concentration [mg/m^3")
    plt.subplot(2,1,2)
    plt.plot(T,V,'x-k')
    #plt.title('Transient Dnamics of reactor')
    #plt.grid("on")
    plt.show()
    # axs[0].plot(T,X,'x-b')
    # axs[0].set_xlabel("Time [s]")
    # axs[0].set_ylabel("Concentration [mg/m^3")
    # axs[1].plot(T,V,'x-k')
    # axs[1].set_xlabel("Time [s]")
    # axs[1].set_ylabel("Concentration [mg/m^3")
    return

def Example2():
# dy2/dt = -k/m*y1 -c/m*y1 + 1/m*f
    def ODE(t,y,m,c,k, Ftable):
        ft = Ftable[0,:]
        Ff = Ftable[1,:]
        F = Pchip(ft,Ff)

        dy2dt = -k/m*y[0] -c/m*y[1] + 1/m*ft
        dy1dt = y[1]

        return np.array([dy2dt,dy1dt])

    m = 20  #kg
    k = 10  #N/m
    c = 5   #N-s/m

    x0 = 0.02 # m
    v0 = 0    # m/s
    y0 = np.array([x0,v0])

    t0 = 0.0    #inital time
    tf = 120.0  #final time
    t_span = np.array([t0,tf])


    Ftable = np.array([[0,25,30,35,120],[0,0,10,0,0]])
    ode = lambda t,y: ODE(t,y,m,c,k, Ftable)

    sol = solve_ivp(ode,t_span,y0, method = 'RK45')

    T=sol.t # time arrarW
    X = sol.y[0,:]
    V = sol.y[0,:]


    
    plt.subplot(3,1,1)
    plt.plot(T,X,'x-b')
    plt.xlabel("Time [s]")
    plt.ylabel("Concentration [mg/m^3")
    plt.subplot(3,1,2)
    plt.plot(T,V,'x-k')
    plt.subplot(3,1,3)
    plt.plot(T,F(T),'x-k')
    plt.show()

    return
Example1()