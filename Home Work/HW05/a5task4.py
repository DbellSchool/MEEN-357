import numpy as np
import matplotlib.pyplot as plt
import GaussElimationSolver as S

h = (1-0.5)/9 # Finds h val

# all rn terms
r0 = 0.5 
r1 = 0.5+h*1
r2 = 0.5+h*2
r3 = 0.5+h*3
r4 = 0.5+h*4
r5 = 0.5+h*5
r6 = 0.5+h*6
r7 = 0.5+h*7
r8 = 0.5+h*8
r9 = 0.5+h*9
r = [r0,r1,r2,r3,r4,r5,r6,r7,r8, r9]

# equation matric 9 terms plus 2 end conditions (11x11)
A = np.array([[0,0.5,0,0,0,0,0,0,0,0,0],
                [2*r0-h,-4*r0,2*r0+h,0,0,0,0,0,0,0,0],
                [0,2*r1-h,-4*r1,2*r1+h,0,0,0,0,0,0,0],
                [0,0,2*r2-h,-4*r2,2*r2+h,0,0,0,0,0,0],
                [0,0,0,2*r3-h,-4*r3,2*r3+h,0,0,0,0,0],
                [0,0,0,0,2*r4-h,-4*r4,2*r4+h,0,0,0,0],
                [0,0,0,0,0,2*r5-h,-4*r5,2*r5+h,0,0,0],
                [0,0,0,0,0,0,2*r6-h,-4*r6,2*r6+h,0,0],
                [0,0,0,0,0,0,0,2*r7-h,-4*r7,2*r7+h,0],
                [0,0,0,0,0,0,0,0,2*r8-h,-4*r8,2*r8+h],
                [0,1,0,0,0,0,0,0,000000,1.000,000000]],dtype= float)

b = np.array([0,0,0,0,0,0,0,0,0,000,200],dtype=float) # end conditions


YTrial = np.linalg.solve(A, np.transpose(b)) #calculates y val   y-1 to y-yn
YTrial_Actual = S.GaussElimationSolver(A,np.transpose(b)) # uses caled gaussElimSolver from file


print("solver:",YTrial,"\nBVP:",YTrial_Actual)