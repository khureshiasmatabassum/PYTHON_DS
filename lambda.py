#s1=lambda x:x*x
#print("the square of a number is:",s1(5))
#print()

#s1=lambda x,y:x+y
#print("the sum of a number is:",s1(6,8))
#print()

#s1=lambda a,b:a if a>b else b
#print("max object:",s1(5,17))



def test_case1(obj1):
   	if(obj1%2==0):
	      return True
       else:
	      return False
if(__name__=="__main__"):
	   obj1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
	   l1=list(filter(test_case1,obj1))
   	print("the result is:",11)