'''
Authour:Ibin Siby
Discription:The while loop is useful for processing input repeatedly until a specific condition is met. In this task, you will:

Use a while loop to continuously ask the user for a number.
Check if the number is odd.
Stop the loop and display a message when an odd number is entered.
'''



while True:
    number=int(input("Enter a number:"))
    if(number%2)!=0:
        print("you entered an odd number:",number)
        break
