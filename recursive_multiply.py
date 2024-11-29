'''
Authour:Ibin Siby
Discription:Recursive function to multiply two positive numbers
'''


def recursive_multiply(num1,num2):
    if num2==1:
        return num1
    else:
        return num1+recursive_multiply(num1,num2-1)

num1 = int(input("Enter number:"))
num2 = int(input("Enter number:"))
result=(recursive_multiply(num1,num2))
print("The product of two numbers is:",result)
