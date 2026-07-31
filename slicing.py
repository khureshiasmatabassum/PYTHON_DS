#positive slicing
#syntax str1[start:stop-1:step]
str1="welcome to nandyal"
print(str1)

#case1
print(str1[0:10])

#case2
print(str1[0:7:2])

#case3
#print(str1[0:7:0])

#case4
#print(str1[0:7:-1])

#case5
#print(str1[::])

#case6
#print(str1[5:3])


#note:  positive slicing the start value should be smaller than the stop value , then only output will get.

#negative slicing

#case1
#print(str1[-1:-8:-1])

#case2
#print(str1[-1:-8:-2])

#case3
#print(str1[-1:-10:-4])

#case4
#print(str1[-4:-2:-1])

#case5
#print(str1[::-1])

#case5
#print(str1[::-1][::-1])


l1=[1,2,3,['a','b',[45,'tcs',20]]]
print(l1[-2])
print(l1[3][2][1])# positive index
print(l1[-1][-1][-1])# negative index


l2=[24,35,67,['abc',[12,56,78,['Ap'],90]],65,98,32,['N','L']]
print(l2[5])
print(l2[3][1][3])#positive index
print(l2[-5][-1][-2])# negative index
print(l2[-3])

#join method is used to convert list into string
l3=(l2[3][1][3])
l4=('').join(l3)
print(l4)
