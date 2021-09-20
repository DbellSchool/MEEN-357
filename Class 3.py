def Tran():
    import numpy as np
    import math as m

    A= np.array([[1,2,3],[4,5,6],[7,8,9]], dtype= float)
    w= np.array([4,5,6], dtype = float)

    print(np.transpose(w))
    print(np.transpose(A))
    print("end")
    return

def mxAdd():
    import numpy as np
    import numpy.linalg as lg
    import math as m

    A= np.array([[1,2,3],[4,5,6],[7,8,9]], dtype= float)
    B= np.array([[10,11,12],[13,14,15],[16,17,18]], dtype = float)

    v = np.array([1,2,3], dtype= float)
    vp =np.array([[1],[2],[3]], dtype= float)


    print("A+w\n",A+B)
    print("A-w\n",np.subtract(A,B))

    print("A/D\n", A / B)

    print("A dot B\n",np.dot(A,B))
    print("A dot V\n",np.dot(A,v))

    print("A dot Vp\n",np.dot(A,vp))


    print("A,b Inner\n", np.inner(A,B))# what does inner do 


    print("the determinant is:\n",A ,"\n Det:\n", lg.det(A))





    print("end")

    return
def Dwt():
    import numpy as np
    import numpy.linalg as lg

    A= np.array([[1,2,3],[1,3,5],[1,4,8]], dtype= float)
    B= np.array([[10,11,12],[13,14,15],[16,17,18]], dtype = float)

    v = np.array([1,2,3], dtype= float)
    vp =np.array([[1],[2],[3]], dtype= float)


    print("A,b Inner\n", np.inner(A,B))# what does inner do 

    print("A,b inverse\n", lg.inv(A))#inverse


    print("the solution is:\n",A ,"\n Det:\n", lg.solve(A,v))
    
    
    return

# error informaiton 
##
##- wrong mo- error in input data
#dles' problem formulation
#- code error/ bugs
#hardware malfuntion( rare but possible)

#intrinsic 
#- roundoff error
#- Truncaion errro
###

#Tran()
#mxAdd()
Dwt()

