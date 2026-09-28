s="pspk"
for x in s: 
     print(x)     
     
str1="core python"
for i in str1:
 	print(i,end='   ')
 	
for x in range(10):
	print(x)	

for y in range(10):
	print("hello world")
	
d1={'AP':'Amaravathi',2:4}
for x,y in d1.items():
	print(x,y)
	
d2={2:4,4:16,8:64}
total=0
for x,y in d2.items():
	print(total+x+y)
	total+=x+y
	print(total)
	
s=input("Enter some String: ")
i=0 
for x in s:
  print("The character present at ",i,"index is :",x)
  i=i+1 
  
#for x in range(21) :
#  if (x%2!=0):
#  	 print(x) 
  	 
#for x in range(10,0,-1):
#	print(x)
	

#list = eval(input("Enter List:"))
#sum=0;
#for x in list:
#	sum=sum+x;
#	print("The Sum=",sum) 
	
import time	
B=0
for x1 in "software developer":
   if(x1 in ("AEIOUaeiou")):
       B=1
       print(x1)
print()
print("The number of vowels in given string:",B)
print()
#time.sleep(2)
#print("end of the application")