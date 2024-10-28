'''
Author:Ibin Siby
Date: 28-10-2024
Discription:a menu-driven Python program that allows users to convert temperatures between Celsius and Fahrenheit. The program should repeatedly display a menu with three options:

   1 Convert Celsius to Fahrenheit
   2Convert Fahrenheit to Celsius
   3 Exit the program

'''
temp=int(input(" Enter temperture:"))
while True:
    print("\n1.\t Convert Celsius to Fahrenheit ")
    print("2.\t Convert Fahrenheit to Celsius")
    print("3.\t exit the program")
    choice=int(input("Enter you choice:"))
    if choice == 1:
       F = (9 / 5 * temp) + 32
       print(temp, "Celcius is", F, "Farenheit")
    elif choice == 2:
        C = (5/9*(temp-32))
        print(temp, "fahrenheit is" ,C, "Celsius" )
    else:
        print("Invalid data")
