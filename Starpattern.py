'''
Authour:Ibin Siby
Discription:Program to construct patterns of stars (*), using a nested for loop.


'''

#Increasing triangle
row1=int(input("Enter the no of rows:"))
for i in range(0,row1):
    for j in range (0,i+1):
        print("*",end="")
    print('')

#Deacreasing triangle
row2=int(input("Enter the no of rows:"))
for k in range(row2,0,-1):
    for l in range (k,0,-1):
        print("*",end="")
    print('')

#Hill Pattern
row3=int(input("Enter the no of rows:"))
for i in range(row3):
    for m in range(i,row3+1):
        print(" ", end=" ")
    for m in range(2*i-1):
        print("*", end=" ")
    print("")


#Reverse hill pattern
row4=int(input("Enter the no of rows:"))
for i in range(row4,0,-1):
    for m in range(row4-i,0,-1):
        print(" ", end=" ")
    for m in range(2*i-1):
        print("*", end=" ")
    print("")



