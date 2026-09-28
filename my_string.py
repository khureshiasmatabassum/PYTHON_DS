str1="welcome to Andhra"
print(str1)
print(type(str1))
#str1[0]="Hello"
print(str1)


#properties
#write value inside the quotatiln marks 
#string is immutable
#string doesn't support item assignment
#we can't add element in existing string

print(str1.split('-')) # split method used to          convert string to list
print(str1)
print(type(str1))
str2=str1.split()
print(str2)
print(type(str2))
print(str1.upper())
print(str1.lower())
print(str1.count('e'))
print(str1.capitalize())
print(str1.rfind('a'))
