class AP:
    def __init__(self):
        print("welcome")

a = AP()
print()

class Nandyal(AP):
    def m1(self):
        print("Nandyal is in AP")
class SN(Nandyal):
	def m2(self):
		print("Srinivasa Nagar")

a = Nandyal()
print()
a.m1()
c=SN()
c.m2()