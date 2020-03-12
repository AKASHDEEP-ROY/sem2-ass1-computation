'''
Assignment-1
problem-5.3
Akashdeep Roy
SVD
'''
import numpy as np
import timeit as t
a=np.array([[0,1,1],[0,1,0],[1,1,0],[0,1,0],[1,0,1]])
print("SVD program")
print((np.linalg.svd(a)))
print("time taken by svd program = ", t.timeit())
s1=np.dot(np.transpose(a),a)
s2=np.dot(a,np.transpose(a))
print("singular values", (np.linalg.eigvals(s1))**0.5)
print("The V matrix")
print(np.linalg.eigh(s1)[1])
print("the U matrix")
print(np.linalg.eigh(s2)[1])
z1=np.linalg.inv(np.linalg.eigh(s1)[1])
z2=np.linalg.inv(np.linalg.eigh(s2)[1])
print("singular matrix")
print(np.dot(np.dot(z2,a),np.transpose(z1)))
t1=t.timeit()
print("time taken by eigvals program = ", t1)