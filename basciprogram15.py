'''
Author:ibin siby
Date:8-11-2024
Discription:find te largest and smallest  second number from a set of numbers
'''

limit=int(input("Enter the limit:"))
number=int(input("Enter the number"))
small=number
big=number
second_small = number
second_big = number
while limit>1:
    number = int(input("Enter the number"))
    if number>big:
        second_big = big
        big=number
    elif number>second_big:
        second_big=number
    if number<small:
        second_small=small
        small=number
    elif number<second_small:
        second_small=number
    limit=limit-1
print("second big", second_big)
print("second small", second_small)


