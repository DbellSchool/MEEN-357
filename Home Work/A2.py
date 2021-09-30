#David Bell
#MEEN 357 HW 2
# Zip name : A2_MEEN357_501_LastName_FirstName.zip

def A2_task1():
    import numpy as np
    import numpy.linalg as lg
    print("Starting Task 1\n")

    A = np.array([[1,2,3,4],[2,4,6,8],[3,6,9,12],[4,8,12,16]], dtype= float)
    C = np.array([[16,12,8,4],[12,9,6,3],[8,6,4,2],[4,3,2,1]], dtype = float)

    b = np.array([[-4],[3],[-2],[1]])
    d = np.array([[-1],[2],[-3],[4]])
    

    x = np.dot((A + np.transpose(A)),b) - np.dot(C,d)

    A_new = np.array([[1,2,3,4],[2,4,6,8],[3,6,9,12],[4,8,12,16]], dtype= float)
    C_new = np.array([[16,12,8,4],[12,9,6,3],[8,6,4,2],[4,3,2,1]], dtype = float)
    c = 0
    for i in A_new: # switches colombs 3 and 4 in A 
        temp = i[2] 
        A_new[c][2] =A_new[c][3]
        A_new[c][3] = temp
        c +=1
    c= 0
    C_new = np.array([[8,6,4,2],[12,9,6,3],[16,12,8,4],[4,3,2,1]], dtype = float) # changed by hand :)

    #for i in C_new: # switches colombs 1 and 3 in A 
    #    temp = i[0] 
    #    C_new[c][0] =C_new[c][2]
    #    C_new[c][2] = temp
    #    c +=1
    x_new = np.dot((A_new + np.transpose(A_new)),b) - np.dot(C_new,d)
    
    M = A + np.transpose(A_new)
    M_max = np.amax(M)
    M_min = np.amin(M)

    print("x is :\n",x)

    print("aNew is:\n",A_new)
    print("cNew is:\n",C_new)
    print("xNew is :\n",x_new,"\n")
    print("mac val is",M_max)
    print("min val is",M_min)
    print(M)
    #print()

    print("End Task 1\n")
    return x, x_new, M_min,M_max





def A2_task2():
    
    from math import sqrt, erf
    from numpy import linspace, cos, sin, pi
    import matplotlib.pyplot as plt
    print("Starting Task 2")
    a = 0.05 # 0.25,0.5,1,1.5
    N = 100

    x = linspace(0,5,num = N)
    y1 = []
    y2 = []
    y3 = []
    y4 = []
    y5 = []
    for i in x:
        y1.append(erf(0.05*i))
    for i in x:
        y2.append(erf(0.25*i))
    for i in x:
        y3.append(erf(0.5*i))
    for i in x:
        y4.append(erf(i))
    for i in x:
        y5.append(erf(1.5*i))
    #print(y,"\n len:", len(y))
    #print("test",erf(a*5))
    alpha = [0.05, 0.25,0.5,1,1.5]
    lgd = [str(i) for i in alpha]
    

    plt.plot(x,y1, '-b')
    plt.plot(x,y2, '--k')
    plt.plot(x,y3, ':c')
    plt.plot(x,y4, '-.m')
    plt.plot(x,y5, '-g')
    plt.legend(lgd, title=r'$\alpha$')
    plt.xlabel("x")
    plt.ylabel("erf(ax)")
    plt.grid("on")

    plt.xlim(0,5)
    plt.show()


    print("End Task 2\n")
    return

def A2_task3():
    from math import sqrt, erf
    from numpy import linspace, cos, sin, pi
    import matplotlib.pyplot as plt
    print("Starting Task 3")
    N = 20

    x1 = linspace(-5,5,num = N)
    y1 = 0.5 *x1**2

    x2 = linspace(0,100,num = N)
    y2 = -x2

    fig, (ax1, ax2) = plt.subplots(2)
    fig.tight_layout(pad=3)
    fig.suptitle('Task 3')

    ax1.plot(x1, y1)
    ax1.set_title("Exhibit 1")
    ax1.set_xlabel("x")
    ax1.set_ylabel("y")

    ax2.plot(x2, y2)
    ax2.set_title("Exhibit 2")
    ax2.set_xlabel("Work")
    ax2.set_ylabel("Play")
    plt.show()

    #ax1.xlabel("x")
    #ax2.ylabel("erf(ax)")



    print("End Task 3\n")
    return
def sort_ascending(Lst):

    for i in range(len(Lst) - 1):
        min = i
        for j in range( i + 1, len(Lst)):
            if(Lst[j] < Lst[min]):
                min = j
        if(min != i):
            Lst[i], Lst[min] = Lst[min], Lst[i]
    return Lst # note change in thing

def A2_task4():
    print("Starting Task 4")
    import random
    #Generate 15 random numbers between -10 and 30
    unsorted_list = []
    for i in range(0,14):
        n = random.randint(1,30)
        unsorted_list.append(n)
    sorted_list = sort_ascending(unsorted_list)
    print(sorted_list)


    print("End Task 4\n")
    return sorted_list

def A2_task5():
    import matplotlib.pyplot as plt
    from math import factorial
    print("Starting Task 5")
    #Taylor eries
    ans = 6.737947e-3

    N = 21
    x = 3

    method_1 = []
    method_2 = []
    Terr_1 = []
    Terr_2 = []
    Aerr_1 = []
    Aerr_2 = []

    

    for n in range(1,N,1):
        y1 = 0
        y2 =0
        for i in range(n):
            y1 += (-1)**i * x**i/factorial(i)    
        method_1.append(y1)
        Terr_1.append(abs((ans-y1)/ans * 100 ))

        for i in range(n):
            y2 += x**i/factorial(i)
        y2 = 1/y2 
        method_2.append(y2)
        Terr_2.append(abs((ans-y2)/ans * 100))

    for i in range(0,len(method_2)):
        if i < len(method_2)-1:
            Aerr_1.append(abs((method_1[i]-method_1[i+1])/method_1[i] * 100))
            Aerr_2.append(abs((method_2[i]-method_2[i+1])/method_2[i] * 100))
###

    fig, (ax1, ax2) = plt.subplots(2)
    fig.tight_layout(pad=3)
    fig.suptitle('Task 5')

    ax1.plot(range(0,len(Terr_1)),Terr_1, label = "eq 1")
    ax1.plot(range(0,len(Terr_2)), Terr_2,label = "eq 2")
    ax1.legend()
    ax1.set_title("T error 1")
    ax1.set_xlabel("err %")
    ax1.set_ylabel("iteration")

    ax2.plot(range(0,len(Aerr_1)), Aerr_1,label = "eq 1")
    ax2.plot(range(0,len(Aerr_2)), Aerr_2,label = "eq 2")
    ax2.legend()
    ax2.set_title(" A error")
    ax2.set_xlabel("err %")
    ax2.set_ylabel("iteration")
    plt.show()

    print("\nEnd Task 5\n")
    return

def A2_task6():
    # trunkation error
    print("Starting Task 6")

    print("\n Task was submitted on paper\n")

    print("End Task 6\n")
    return

print("working")

A2_task2()