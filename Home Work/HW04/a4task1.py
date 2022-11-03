
import numpy as np
import matplotlib.pyplot as plt

def func(x): # test func
    y = x**2*np.exp(x)
    #y = x

    return y


def trapint(x, fx):
    if len(x) != len(fx):
        raise Exception('the input imintions so not match') # confirms lenth is the same
    elif isinstance(x[0], list) or isinstance(x[0], np.ndarray): # check if the first elemtn is a list
        raise Exception('the input for x is not a 1d array')
    elif isinstance(fx[0], list) or isinstance(fx[0], np.ndarray): # check if the first elemtn is a list
        raise Exception('the inputs for fx is not a 1d array')
    
    A =0 # starts count
    for i in range (len(x)-1):
        A += 0.5*(fx[i] + fx[i+1])*(x[i+1] - x[i]) # finds area between two indexes
    
    return A




# Test Code:

'''
rb = 3
lb = 0

x = np.linspace(lb,rb,10000)
y = func(x)

a = trapint(x, y)

print(a)
'''
# Plotting code
def plot():
        
    Tv = 98.42768462 # acutal val from calculator

    # bounds
    rb = 3
    lb = 0

    # number of integrations
    N = 30
    A = []
    for n in range(2,N):
        x = np.linspace(lb,rb,n)
        y = func(x)

        a = trapint(x, y)
        A.append(a)

    NN = np.arange(2,N)

    TV = []
    for i in range(len(NN)): #creates aline form acutle value --> calcualted usign calcualtor
        TV.append(Tv)

    #plots data
    plt.plot(NN,TV, label = 'True Val')
    plt.plot(NN,A, label='function')
    plt.legend()
    plt.xlabel('sections [x]')
    plt.ylabel('intigral [x*y]')
    plt.show()

    return

plot()