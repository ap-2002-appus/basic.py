'''
Authour:Ibin Siby
Discription:Python program to
1.Ask the user for their name.
2.Ask the user for their age (in years).
3.Calculate their age in months (multiply their age by 12).

Display a message that includes:
Their name.
Their age in years.
Their age in months.
'''


name=str(input("Enter your name:"))
age=int(input("Enter your age(in years):"))
age_in_months=(age*12)
print("Hello,",name)
print("You are",age,"years old,which is",age_in_months,"months.")


