# previously Explisate etho
# Runge-huttea methosd in python (first order)
# heun's mehtodd (secondn order) 
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt # for plot
import numpy as np

# deful is rk 24 --> 4th order rancarder ith 5th order step soze
# Rk 23 secn order ankater methos wiht 3rd order method
# DOP 853 ecplicit Runge-kutta method od oreder

def odefun(t,y,cin = 50,Q = 5,V=100):

    c = y
    dydt = 1/V*(Q*cin-Q*c)

    return dydt

def run1():

    t0 = 0.0
    tf = 50.0

    c0 = 10 
    y0 = np.array([c0])
    t_span = [t0,tf]


    sol = solve_ivp(odefun,t_span,y0,method = 'RK45')

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
#run1()

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
