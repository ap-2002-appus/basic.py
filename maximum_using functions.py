'''
Authour:Ibin Siby
Discription: Write a Python function to find the maximum of three numbers.
'''


def number(list):
    list.sort()
    print(f"The maximum value is:{list[2]}")
num1=int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
num3 = int(input("Enter third number:"))
list=[num1,num2,num3]
number(list)