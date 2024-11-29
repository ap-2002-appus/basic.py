'''
Authour:Ibin Siby
Discription:Program to find the factorial of a number using Recursion.
'''
def factorial(n):
    if n==0:
        return 1
    else:
        return(n*factorial(n-1))
f=int(input("Enter number:"))
n=factorial(f)
print("Factorial of given number",f, "is", n)