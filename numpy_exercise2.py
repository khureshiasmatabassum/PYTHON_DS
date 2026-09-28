#how to solve linear expression using numpy
#2x+y=5
#x+3y=6
import numpy as np
#coefficient matrix
A=np.array([
[2,1],
[1,3]
])
#constant values
B=np.array([5,6])
#solve AX=B
solution=np.linalg.solve(A,B)
print("coefficient matrix A:")
print(A)
print("\constant matrix B:")
print(B)
print("\solution:")
print(solution)
print("\nvalue of x:",solution[0])
print("value of y:",solution[1])


#2x+y+z=6
#x+3y+z=7
import numpy as np
# Coefficient matrix
A = np.array([
    [2, 1, 1],
    [1, 3, 1]
])
# Constant values
B = np.array([6, 7])
# Solve AX = B
solution = np.linalg.lstsq(A, B, rcond=None)[0]
print("Coefficient matrix A:")
print(A)

print("\nConstant matrix B:")
print(B)

print("\nSolution:")
print(solution)

print("\nValue of x:", solution[0])
print("Value of y:", solution[1])
print("Value of z:", solution[2])


#2x+y+z
#x+3y+2z
#4x+y+2x
import numpy as np
#coefficient matrix
A=np.array([
[2,1,1],
[1,3,2],
[4,1,2]
])
#constant values
B=np.array([8,10,14])
#solve AX=B
solution=np.linalg.solve(A,B)
print("coefficient matrix A:")
print(A)
print("\constant matrix B:")
print(B)
print("\solution:")
print(solution)
print("\nvalue of x:",solution[0])
print("value of y:",solution[1])
print("value of z:",solution[2])
