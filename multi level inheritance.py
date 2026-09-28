import time 
class I_HUB1:
    def m1(self):
        print("IHUB one services ...")
class I_HUB2(I_HUB1):
    def m2(self):
        print("IHUB two services ...")
class I_HUB3(I_HUB2):
    def m3(self):
        print("IHUB three services ...")
class I_HUB4(I_HUB3):
    def m4(self):
        print("IHUB four services ...")
i1=I_HUB2()
i1.m1()
i1.m2()
print()
i2=I_HUB3()
i2.m1()
i2.m2()
i2.m3()
print()
i3=I_HUB4()
i3.m1()
i3.m2()
i3.m3()
i3.m4()
print()
time.sleep(2)
print('End of an application....')
