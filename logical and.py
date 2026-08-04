#AND logic is two conditional check 
#1 1 1
#1 0 0
#0 1 0
#0 0 0
#OR logic is to check multiple conditions ( check box)
#1 1 1
#0 1 1
#1 0 1
#0 0 0
import time 
print("---WELCOME TO IHUB FOR  SOFTWARE SERVICES---")
username=input("Enter the username:")
password=input("Enter the password:")
if(username=="rahul_123" and password=="_12345"):
    print(username,password,"--->Welcome to IHUB for IT services")
else:
    print(username,password,"--->Dear user please enter the valid datials")
print()
time.sleep(2)
print("End of an application")

