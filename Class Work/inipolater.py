from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import numpy as np

xData = [3.0,4.5,7.0,9]
yData = [2.5,1,2.5,0.5]

fcubic = interp1d(xData,yData,kind = "cubic")
fcubic2 = interp1d(xData,yData,kind = "quadratic")

x = np.linspace(3,9,100)
y =fcubic(x)
y2 = fcubic2(x)

plt.plot(xData,yData,"*r")
plt.plot(x,y,"-b")
plt.plot(x,y2,"-k")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(["data", "cubic splines","Quadradtic"])
plt.grid()

plt.show()