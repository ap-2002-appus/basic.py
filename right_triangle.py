'''
Authour:Ibin Siby
Discription:
A program that accepts the lengths of three sides of a triangle as inputs. The program should output whether or not the triangle is a right triangle (Recall from the Pythagorean Theorem that in a right triangle, the square of one side equals the sum of the squares of the other two sides). Implement using functions.
Example Runs:
Example 1
    Enter the length of the first side: 3
    Enter the length of the second side: 4
    Enter the length of the third side: 5
    The given triangle is a right triangle.

Example 2:
    Enter the length of the first side: 2
    Enter the length of the second side: 3
    Enter the length of the third side: 4
    The given triangle is not a right triangle.
'''
def sides (first,second,third):
    list=[first,second,third]
    print(list)
    list.sort()
    if list[2]**2 == list[0]**2 + list[1]**2:
        print("This is a right angled triangle")
    else:
        print("This is not a right angled triangle")
a=int(input("Enter first side:"))
b=int(input("Enter second side:"))
c=int(input("Enter third side:"))
sides(a,b,c)