'''
Author:Ibin Siby
Date:28-10-2024
discription: program that simulates a simple bank ATM system. The user has an initial balance of $1000. The ATM should display a menu with options to:

    Check Balance
    Deposit Money
    Withdraw Money
    Exit

The program should run in a loop until the user chooses to exit. For each option, use if, elif, and else to manage each choice. Ensure that the balance doesn’t go below zero during a withdrawal.

'''
balance_amount=1000
while True:
    print("\n1.\t Check Balance")
    print("2.\t Deposit Money")
    print("3.\t Withdraw Money")
    print("4.\t Exit")
    choice=int(input("Enter you choice:"))
    if choice == 1:
        print(f"The current balance ${balance_amount}")
    elif choice == 2:
        Deposit_amount= float(input("Enter the amount"))
        balance_amount= balance_amount + Deposit_amount
        print(f"The deposited amount ${Deposit_amount} and " f"the current balance ${balance_amount}")
    elif choice ==3:
        withdraw_amount = float(input("Enter the amount to withdraw"))
        if (withdraw_amount>balance_amount):
            print("insufficient_balance")
        else:
            Balance_amount= balance_amount - withdraw_amount
            print("sufficient_balance")
            print(f"The amount withdraw from the account " f"${withdraw_amount} the balance amount" f"${balance_amount}")

    elif choice == 4:
        break
    else:
        print("Invalid Entry")

