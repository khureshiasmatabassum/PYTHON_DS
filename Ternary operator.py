# if condition is true then first value will be considered else second value will be considered.
#a,b=20,10
#x=30 if a<b else 40
#print(x)

#a=int(input("enter the first number:"))
#b=int(input("enter the second number:"))
#min=a if a<b else b
#print("minimun value:",min)

#a=int(input("Enter First Number:")) 
#b=int(input("Enter Second Number:")) 
#c=int(input("Enter Third Number:")) 
#min=a if a<b and a<c else b if b<c else c
#print("Minimum Value:",min)

a=int(input("Enter First Number:"))
b=int(input("Enter Second Number:")) 
c=int(input("Enter Third Number:")) 
max=a if a>b and a>c else b if b>c else c 
print("Maximum Value:",max) 