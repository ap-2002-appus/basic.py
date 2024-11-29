'''
Authour:Ibin Siby
Discription:python Program to check whether the given number is a valid mobile number or not using functions.

Rules:

    Every number should contain exactly 10 digits.
    The first digit should be 7 or 8 or 9
'''


def number(n):
    if len(n) and n[0] in "987":
        print(f"The mobile number is {n} is Valid.")

    else:
        print(f"The mobile number is {n} is Invalid.")
number(input("Enter mobile number:"))