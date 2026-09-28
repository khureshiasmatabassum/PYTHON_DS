import time 
class Mother_Class:
    def m1(self):
        print("Mother class implementation ...")
class Son1(Mother_Class):
    def m2(self):
        print("Son1 one class implementation ...")
class Son2(Mother_Class):
    def m3(self):
        print("Son2 two class implementation ...")
class Son3(Mother_Class):
    def m4(self):
        print("Son3 three class implementation ...")
s1=Son1()
s1.m1()
s1.m2()
print()
s2=Son2()
s2.m1()
s2.m3() 
print()
s3=Son3()
s3.m1()
s3.m4()
print()
time.sleep(2)
print("End of an application")
