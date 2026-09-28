import time
str1=input("enter the string object:")
x=0
A=0
while(x<len(str1)):
	if(str1[x] in ("AEIOUaeiou")):
		A+=1
		print(str1[x])
	x+=1
print()
print("vowels present in given string is:",A)
print()
time.sleep(2)
print("end of the application")

