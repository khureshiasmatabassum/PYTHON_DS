d1={'AP':'Amaravathi',"AP":'Guntur','MH':'Mumbai',2:4,8:64,2:16}
print(d1)
print(type(d1))
print(d1.keys())
print(d1.values())
# dictionary is represented in curly brackets
# in dictionary duplicate keys are not allowed

#Dictionary methods
#1.get()
print(d1.get('AP'))

#2.popitem()
print(d1.popitem())
print(d1)

#setdefault
d2="Name","Asma"
d1.setdefault(d2)
print(d1)
print(d1.setdefault(9,"hello")) #correct way to add elements key & value pair in dictionary
print(d1)

#pop()
d5={"india":"new delhi","USA":"new york",'KA':'Banglore','KA':'hubli',2:8,2:16}
print(d5)
print(d5.pop(2))
print(d5)

d6=d5.copy()
print(d6)