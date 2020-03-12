'''
Akashdeep Roy
DAA
Solving a system of linear equations using Relaxation method.
'''
#importing the library functions
import numpy as np
#input zone
err=0.01    #The accuracy limit
sol=np.array([7.85971,0.422926408,-0.073592239,-0.540643016,0.010626163]) #The solution given
a=np.array([[0.2,0.1,1,1,0],[0.1,4,-1,1,-1],[1,-1,60,0,2],[1,1,0,8,4],[0,-1,-2,4,700]],dtype=float) #The coefficient matrix
b=np.array([1,2,3,4,5],dtype=float) #The 0-power coefficient column
x=np.array([0,0,0,0,0],dtype=float)
#computation zone
i=0
while(np.any(abs(x-sol)>=err)):
   p=np.copy(x)
   x=np.zeros(5)
   r=np.zeros(5)
   
   for j in range(5):   
       for k in range(5):
           if k<j :
               x[j]=x[j]-(a[j,k]*x[k])
           if k>j:
                x[j]=x[j]-(a[j,k]*p[k])
       r[j]=(b[j]+x[j])/a[j,j]-p[j]
       x[j]=p[j]+1.25*r[j]
   i=i+1
#output zone
print("solution is: ")
print(x)
print("iteration required to converge =", i)
   