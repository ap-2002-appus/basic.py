'''
Authour:Ibin Siby
Discription:a program that asks for the user's age.
Use if and if-else statements to print:
"Child" if age is less than 13.
"Teen" if age is between 13 and 19.
"Adult" if age is between 20 and 64.
"Senior" if age is 65 or older.


'''
age=int(input("Enter your age:"))
if(age<13):
    print("You are a Child")
elif(age>13 and age<19):
    print("You are a Teen")
elif(age>20 and age<64):
    print("You are an Adult")
else:
    print("You are a Senior")

