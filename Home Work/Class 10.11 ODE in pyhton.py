# previously Explisate etho
# Runge-huttea methosd in python (first order)
# heun's mehtodd (secondn order) 
from scipy.integrate import solve_ivp

# deful is rk 24 --> 4th order rancarder ith 5th order step soze
# Rk 23 secn order ankater methos wiht 3rd order method
# DOP 853 ecplicit Runge-kutta method od oreder

def odefun(t,y,cin,Q,V):
    cin = 50
    Q = 5
    V =100

    c = y
    dydt = 1/V*(Q*cin-Q*c)

    return dydt

t_span = 3
y0 = 1

sol = solve_ivp(odefun,t_span,y0,method = 'RK45')

T=sol.t # time arrar
Y = sol.y # solutoin arat
TE = sol.t_events # events not caputed
YE = sol.y_events