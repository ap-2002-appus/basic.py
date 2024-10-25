'''
Author:Ibin Siby
Date:25-10-2024
Discription:Phython program to print the Sum of digits of the given number.
'''
number=int(input("Enter a number:"))
sum_of_digits=0
while number>0:
    remainder = number%10
    sum_of_digits = sum_of_digits+remainder
    number=number//10
print("Sum of digits of the given number:",sum_of_digits)