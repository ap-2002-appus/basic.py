'''
Author:Ibin Siby
Date :25-10-2024
discription:python program for checking the given number is possitive or negative


'''
number1=int(input("Enter first number:"))
number2=int(input("Enter second number"))
number3=int(input("Enter third number"))

if(number1>number2 and number1>number3):
    print("number1 is greater is greater than other two")
elif(number2>number1 and number2>number3):
    print("number2 is greater is greater than other two")
else:
    print("number3 is greater is greater than other two")

