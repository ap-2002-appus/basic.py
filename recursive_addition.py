'''

Authour:Ibin Siby
Discription:Recursive function to add two positive numbers.
'''

def recursive_add(num1,num2):
    if num2==0:
        return num1
    else:
        return recursive_add(num1+1,num2-1)
num1=int(input("Enter number:"))
num2=int(input("Enter number:"))
print("Sum=",recursive_add(num1,num2))