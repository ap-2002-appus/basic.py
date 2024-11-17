'''
Authour:Ibin Siby
Discription: python program calculator that performs a basic operation chosen by the user.

Instructions:
1.Ask the user to enter two numbers.
2.Ask the user to choose an operation: add, subtract, multiply, or divide.
3.Use if-elif-else statements to perform the chosen operation and display the result.
'''



first_number=int(input("Enter the first number:"))
second_number=int(input("Enter the second number:"))
operator=input("Choose an operater (+, -, *, /):")
if operator=="+":
    print("The result is:",first_number+second_number)
elif operator=="-":
    print("The result is:",second_number-first_number)
elif operator=="*":
    print("The result is:",first_number*second_number)
elif operator=="/":
    print("The result is:",second_number/first_number)
else:
    print("invalid operator")