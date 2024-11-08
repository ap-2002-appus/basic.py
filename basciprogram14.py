'''
Author:ibin siby
Date:8-11-2024
Discription:find te largest and smallest number from a set of numbers
'''

limit=int(input("Enter the limit:"))
number=int(input("Enter the number"))
small=number
big=number
while limit>1:
    number = int(input("Enter the number"))
    if number>big:
        big = number
    if number<small:
        number=small
    limit=limit-1
print("big", big)
print("small", small)

