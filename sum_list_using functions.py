'''
Authour:Ibin Siby
Discription:  Write a Python function to sum all the numbers in a list.
'''

def sum_of_list(list):
    sum=0
    for i in list:
        sum=sum+i
    print(sum)
list=[]
n=int(input("Enter the number of elements:"))
for i in range(n):
    b=int(input("Enter the element: "))
    list.append(b)
sum_of_list(list)