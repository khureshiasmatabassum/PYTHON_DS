import time 
class Parent_One:
    def m1(self):
        print("Parent one class implementation")
class Parent_Two:
    def m2(self):
        print("Parent two class implementation ")
class Parent_Three:
    def m3(self):
        print("Parent three class implementation")
class Parent_Four:
    def m4(self):
        print("Parent four class implementation")
class Child_one(Parent_One,Parent_Two,Parent_Three,Parent_Four):
    def m5(self):
        print("Child one class implemenation")
c1=Child_one()
c1.m1()
c1.m2()
c1.m3()
c1.m4()
c1.m5()
print()
time.sleep(2)
print('End of an application')