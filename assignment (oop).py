class A:
    def show(self):
        print("Class A")

class B(A):
    def display(self):
        print("Class B")

b = B()
b.show()
b.display()


class Parent:
    def msg(self):
        print("Parent")

class Child(Parent):
    pass

c = Child()
c.msg()


class A:
    def a(self):
        print("A")

class B(A):
    def b(self):
        print("B")

class C(B):
    def c(self):
        print("C")

x = C()
x.a()
x.b()
x.c()



class A:
    def show(self):
        print("A")

class B(A):
    pass

class C(A):
    pass

B().show()
C().show()


class A:
    def show(self):
        print("A")

class B(A):
    pass

class C(A):
    pass

B().show()
C().show()



class A:
    def a(self):
        print("A")

class B:
    def b(self):
        print("B")

class C(A, B):
    pass

c = C()
c.a()
c.b()



class A:
    def __init__(self):
        print("Welcome")

class B(A):
    pass

b = B()



class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        super().show()
        print("B")

b = B()
b.show()



class A:
    def show(self):
        print("Parent")

class B(A):
    def show(self):
        print("Child")

b = B()
b.show()



class Student:
    def name(self):
        print("Asma")

class Marks(Student):
    def marks(self):
        print("90")

s = Marks()
s.name()
s.marks()




class Employee:
    def details(self):
        print("Employee")

class Salary(Employee):
    def pay(self):
        print("30000")

s = Salary()
s.details()
s.pay()