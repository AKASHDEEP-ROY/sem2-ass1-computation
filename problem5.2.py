'''
Assignment-1
problem-5.2
Akashdeep Roy
Finding dominant eigenvalue & corresponding eigenvector using power method
'''
import numpy as np
x=np.array([2,3,7])
y=np.array([5,7,1])
A=np.array([[2,-1,0],[-1,2,-1],[0,-1,2]])
v=np.copy(A)

w=1
err=0.00001

j=0
while (w==1):
    p=np.dot(v,A)                                   
    s=np.dot(p,A)
    u=np.dot(y,np.dot(s,x))/np.dot(y,np.dot(p,x))   
    q=np.dot(y,np.dot(p,x))/np.dot(y,np.dot(v,x))   
    if (abs(u-q))<err:
        print("dominant eigenvalue = ", q)
        print("normalized eigenvector associated with dominant eigenvalue = ", np.dot(v,x)/np.linalg.norm(np.dot(v,x)))
        print("no of iteration = ", j)
        w=0
    v=p
    j=j+1  