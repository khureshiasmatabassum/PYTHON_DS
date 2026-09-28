#def test_case1(*a):
#	for x1 in a:
#		print(x1)
#if(__name__=="__main__"):
#	test_case1("rahul","verma","rahul_12345","_12345","rahul@gmail.com")
#	print()
	
	
def test_employee_case1(**a):
	for x1,y1 in a.items():
		print(x1,"==",y1)
if(__name__=="__main__"):
     test_employee_case1(name="rahul",surname="verma",username="rahul_12345",password=12345,email="rahul@gmail.com")
print()