#David Bell
#MEEN 357 HW 2
# Zip name : A2_MEEN357_501_LastName_FirstName.zip

def A2_task1():
    import numpy as np
    import numpy.linalg as lg

    A= np.array([[1,2,3,4],[2,4,6,8],[3,6,9,12],[4,8,12,16]], dtype= float)
    C= np.array([[16,12,8,4],[12,9,6,3],[8,6,4,2],[4,3,2,1]], dtype = float)

    b = np.array([-4,3,-2,1])
    d = np.array([-1,2,-3,4])
    
    x = np.dot((A + np.transpose(A)),b) - np.dot(C,d)
    print(x)
    
    return
A2_task1()

def A2_task2():
    
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
    return

def A2_task3():

    return

def A2_task4():



    return

def A2_task5():



    return

def A2_task6():
    # trunkation error


    return

