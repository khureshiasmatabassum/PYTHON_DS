import numpy as np
#coefficient matrix
A=np.array([
[2,3],
[1,1]
])
#constanet matrix
B=np.array([8,3])
#solve the lineae expressions
solution=np.linalg.solve(A,B)
print("Solution:")
print("x =", solution[0])
print("y =", solution[1])