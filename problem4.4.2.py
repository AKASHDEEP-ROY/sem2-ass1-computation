'''
Assignment-1
Problem-4.4.2
Akashdeep Roy
Solve a system of linear equations in iterative process using Gauss-Seidel method
'''
from numpy import *
#user input
A_1=array([[0.2,0.1,1,1,0],[0.1,4,-1,1,-1],[1,-1,60,0,-2],[1,1,0,8,4],[0,-1,-2,4,700]])    #coefficient matrix
B_1=array([1,2,3,4,5])     #0-power coefficient column
X2_empty=array([0.0,0.0,0.0,0.0,0.0])   #initial guess
sol=array([7.859713071,0.422926408,-0.073592239,-0.540643016,0.010626163])   #solution given
err=0.01    #accuracy limit


X1_empty = zeros(5)
w=1
iteration=0

while(w==1): 
  #initializing p = [0,0,...]  
    p_empty=zeros(5)    
  #doing the algebra
    for i in range(5):
      for j in range(5):
        if j!=i :  
          p_empty[i]=p_empty[i]+((A_1[i][j])*(X2_empty[j]))
      X2_empty[i]=(B_1[i]-p_empty[i])/A_1[i][i]
  #comparison so that solution saturates within error bound
    
    t=0
    for i in range(5):
      if (abs(X2_empty[i]-sol[i]))<err :
        t=t+1
    if t == 5 :
      print("iteration=",iteration)
      print(X2_empty)
      w=0
    else:
        X1_empty=copy(X2_empty)
        iteration=iteration+1

