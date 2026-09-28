import numpy as np
s1=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print()
print(s1)
print()
d2=s1.reshape(6,2)
print("the result is:",d2)
print()
print("the dimensions are:",s1.ndim)
for x1 in d2:
	for y1 in x1:
		print(y1,end=" ")
		print()
		print()