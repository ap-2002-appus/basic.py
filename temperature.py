'''
Author-Ibin Siby
Date-25/10/2024
Discription-Write a Python program to convert temperature values back and forth between Celsius and Fahrenheit. The user should be able to input a temperature in Celsius or Fahrenheit, and the program should convert it to the other unit using the formula:
c5=f−329

    For Celsius to Fahrenheit conversion:
    f=(95×c)+32

    For Fahrenheit to Celsius conversion:
    c=59×(f−32)

'''

temp=int(input(" Enter temperture:"))
units=str(input("Is this in (C)elsius or (F)ahrenheit"))
F=(9/5*temp)+32
if units=='C':

    print(temp,"Celcius is",F,"Farenheit")
else:
    g=5/9*(temp-32)
    print(temp,"Farenheit is",g,"Celcius")

