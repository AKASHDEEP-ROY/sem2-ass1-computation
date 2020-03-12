'''
Assignment-1
problem 4.4.4
Akashdeep Roy
DAA
Soving a system of linear equations using Conjugate-Gradient method
'''
#importing the library functions
import numpy as np
#input zone
a=np.array([[0.2,0.1,1,1,0],[0.1,4,-1,1,-1],[1,-1,60,0,-2],[1,1,0,8,4],[0,-1,-2,4,700]])    #coefficient matrix
b=np.array([1,2,3,4,5])     #0-power coefficient column
x=np.array([0,0,0,0,0])   #initial guess
sol=np.array([7.859713071,0.422926408,-0.073592239,-0.540643016,0.010626163])   #solution given
err=0.01    #accuracy limit
#computation zone with output
r=b-np.dot(a,x)
p=r
ro=np.dot(np.transpose(r),r)
w=1
k=0
while(w==1):
    q=((np.dot(np.transpose(r),r))/np.dot(np.transpose(p),np.dot(a,p)))
    x=x+(q*p)
    if (all(abs(sol[i]-x[i])<err for i in range(5))):
        print("solution", x)    #output
        print("iteration", k)
        w=0
    h=r-q*np.dot(a,p)
    z=(np.linalg.norm(h)/np.linalg.norm(r))**2
    r=np.copy(h)
    p=r+z*p
    k=k+1