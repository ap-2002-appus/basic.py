'''
Authour:Ibin Siby
Discription:  Write a Python function to multiply all the numbers in a list.
'''

def mul_of_list(list):
    mul=1
    for i in list:
        mul=mul*i
    print(mul)
list=[]
n=int(input("Enter the number of elements:"))
for i in range(n):
    b=int(input("Enter the element: "))
    list.append(b)
mul_of_list(list)