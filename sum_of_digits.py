'''
Authour:Ibin Siby
Discription:python program for breaking down a number into its individual digits can be done using loops and arithmetic operations. In this task, you will:

1.Ask the user for a positive integer.
2.Use a loop to extract each digit of the number.
3.Add the digits together to calculate the total sum.
4.Print the result.

'''
number=int(input("Enter a positive integer: "))
sum_of_the_digits=0
while number>0:
    last_digit=number%10
    sum_of_the_digits=sum_of_the_digits+last_digit
    number//=10
print("The sum of the digits is:",sum_of_the_digits)