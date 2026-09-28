import time 
class Quality_Thought:
    def m1(self):
        print("It is parent company ...")
class I_HUB(Quality_Thought):
    def m2(self):
        print("It is child company")
print()
q1=Quality_Thought()
q1.m1()
i1=I_HUB()
print()
i1.m1()
print()
i1.m2()
print()
time.sleep(2)
print("End of an application")


