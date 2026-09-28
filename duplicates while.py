import time
list_one=eval(input('enter the list data type:'))
res1=[]
a=0
while(a<len(list_one)):
	if(list_one[a] not in res1):
		res1.append(list_one[a])
	a+=1
print()
print("my list object with duplicate values:",list_one)
print()
print("after removing the duplicate objects:",res1)
print()
time.sleep(2)
print("end of the application")
	