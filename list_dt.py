l1=[1,2,3.4,'abc']
print(l1)
print(type(l1))

# 3 methods to add elements in list
#1 Append
l1.append(4)
print(l1)

#2 extend
l1.extend([7,8,9])
print(l1)

#3 insert
l1.insert(0,'asma')
print(l1)
print()

# 3 methods to delete or remove elements in list
#1.pop
l2=[1,2,3]
print(l2)
print()
l2.pop()
print(l2)

#2.remove
l2.remove(2)
print(l2)


#3.clear
l2.clear()
print(l2)

#reverse
l5=[1,2,6,3,2,80,75,43] 
print(l5)
l5.reverse()
print(l5)

#sorting
l5.sort() # Ascending order
print(l5)
l5.sort(reverse=True) # Descending order
print(l5)
l6=l5.copy()
print(l6)
print(len(l5))
l6=['abc','def']
print(l6)
print(type(l6))
l7=('').join(l6)
print(l7)
print(type(l7))
l8=[1,2,3,4,5]
l9=('').join(map(str,l8)) #mapping
print(l9)