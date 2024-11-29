'''
Authour:Ibin Siby
Discription:Recursive function to find the greatest common divisor of two positive numbers.
'''


def gcd(num1,num2):
    if num1%num2==0:
        return num2
    else:
        return gcd(num2,num1%num2)
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
print("The greatest common divisor of",num1,num2,"is:",gcd(num1,num2))

