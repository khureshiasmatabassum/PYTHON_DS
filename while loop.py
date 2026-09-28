#infinite loop
i=1
while i<=5:
   print("Hello")
   i=i+1
   
i=5
while i>=1:
	print(i) 
	i-=1
	
#Reverse the string
n=input("enter string")
str2=" "
i=0
while i<len(n):
	str2=n[i]+str2
	i=i+1
print(str2)
	

for i in range(len(n)):
	print(n[i])
	
str1=input("enter the string object:")
a=0
while(a<len(str1)):
	print(a,"----",str1[a])
	a+=1
print()




	