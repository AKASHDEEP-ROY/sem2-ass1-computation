# Assignment-1
# Problem-1.2
# Akashdeep Roy
# Solve a system of linear equations using numpy.linalg.solve

# importing library needed
import numpy as np
#Define the square matrix A & column vector B 
A=np.array([[1,0.67,0.33],[0.45,1,0.55],[0.67,0.33,1]])
B=np.array([2,2,2])
# The output gives the solved values for x1,x2,x3 in an array named X
X=np.linalg.solve(A,B)
print(X)

# Ans : 1,1,1 respectively
# end