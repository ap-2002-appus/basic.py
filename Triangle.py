'''
Authour:Ibin Siby
Discription: Python program to find the shape of the triangle by inserting the length of three sides of the triangle.

'''

First_side=int(input("Enter the length of first side:"))
Second_side=int(input("Enter the length of second side:"))
Third_side=int(input("Enter the length of third side:"))
if(First_side==Second_side==Third_side):
    print("Equilateral")
elif(First_side==Second_side or Second_side==Third_side):
    print("Isoceles")
elif(First_side!=Second_side!=Third_side):
    print("Scalene")
else:
    print("Not a triangle")