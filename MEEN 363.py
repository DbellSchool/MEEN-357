# Code 9.15.21
from math import sqrt
from numpy import linspace, cos, sin, pi
import matplotlib.pyplot as plt


m = 40
k = 5.385*10**6
g = 9.81
v0 = 0.1
y0 = 0

T= 0.05
N = 100

wn = sqrt(k/m)

t = linspace(0,T,N)
y = (y0-m*g/k)*cos(wn*t) + v0/wn*sin(wn*t) + m*g/k

plt.plot(t,y, '-r')
plt.xlabel("Time [sec]")
plt.ylabel("Y [m]")
plt.grid("on")

plt.xlim(0,T)

plt.show()

print("{ttau}_n = {:f}",format(2*pi/wn))


