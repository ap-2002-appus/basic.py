'''
Authour:Ibin Siby
Discription:Python program to print the tip amount based on a given bill amount and tip percentage.

Description:
This task will reinforce basic arithmetic and variable usage. You’ll ask the user for the bill amount and tip percentage, calculate the tip, and display the total amount to be paid.

Instructions:

1.Ask the user to enter the bill amount.
2.Ask the user to enter the tip percentage they would like to leave (e.g., 15 for 15%).
3.Calculate the tip using the formula: tip = (bill * tip_percentage) / 100.
4.Print the calculated tip and the total bill amount, which is the sum of the bill and the tip.
'''



bill_amount=int(input("Enter the bill amount:"))
tip_per=int(input("Enter the tip percentage:"))
tip=(bill_amount*tip_per)/100
total_bill=(bill_amount+tip)
print("Tip amount:",tip)
print("Total amount to be paid:",total_bill)