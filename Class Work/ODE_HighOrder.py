# first order f(ty)
# second order  ODE (t,y)
#d^ny/dt^b  nth order oder  h(t,y)

##################################################
# Example: Second Order Mass Damper No Exitation #
##################################################
# lecture 15 spring mass dampnetr system
# How do we find the response using th first order solver
# Create multible first order Equations

from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt # for plot
import numpy as np


def Motion_ODE_SpringMassDamp(t,y,m,k,c):
    dy1dt= y[1]
    dy2dt = -k/m*y[0]-c/m*y[1]

    dydt = np.array([dy1dt,dy2dt])


    return dydt

def run1():
    m = 20
    k=20
    c =5
    x0 = 0.01
    v0 = 0.0
    y0 =  np.array([x0,v0])

    t0 = 0.0
    tf = 120
    t_span = [t0,tf]

    fun = lambda t,y: Motion_ODE_SpringMassDamp(t,y,m,k,y) # makes it a function with only two inputs

    sol = solve_ivp(fun,t_span,y0,method = 'RK45')

    T=sol.t # time arrar
    
    X = sol.y[0,:]
    V = sol.y[1,:]

    print(sol.y[0,:]) # list in th e nested array ( only gave y and t is not uses so list on onley values varis with y)

    TE = sol.t_events # events not caputed
    YE = sol.y_events

    plt.plot(T,y,'x-b')
    plt.xlabel("Time [s]")
    plt.ylabel("Concentration [mg/m^3")
    plt.title('Transient Dnamics of reactor')
    plt.grid("on")
    plt.show()


    return





def run2():

    t0 = 0.0
    tf = 50.0

    c0 = 10 
    y0 = np.array([c0])
    t_span = [t0,tf]

    cin = 50
    Q = 5
    V=100
    fun = lambda t,y: odefun(t,y,cin,Q,V) # makes it a function with only two inputs

    sol = solve_ivp(fun,t_span,y0,method = 'RK45')

    T=sol.t # time arrar
    Y = sol.y # solutoin arat
    y = sol.y[0,:]

    print(sol.y[0,:]) # list in th e nested array ( only gave y and t is not uses so list on onley values varis with y)

    TE = sol.t_events # events not caputed
    YE = sol.y_events

    plt.plot(T,y,'x-b')
    plt.xlabel("Time [s]")
    plt.ylabel("Concentration [mg/m^3")
    plt.title('Transient Dnamics of reactor')
    plt.grid("on")
    plt.show()
run2()