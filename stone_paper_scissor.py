'''
Authour:Ibin Siby
Discription:python programto play stone,paper and scissors
'''
import random
while True:
    options=["rock","paper","scissors"]
    choice=(input("your options are rock,paper or scissors\n[type 'exit' to quit]\nchoose!:"))
    choice=choice.lower()
    if choice=="exit":
        break
    selection=random.choice(options)
    print("the computer chooses",selection)
    if choice=='scissor' and selection=='paper':
        print("you win")
    elif choice=='paper' and selection=='rock':
        print("you win")
    elif choice=='stone' and selection=='scissors':
        print("you win")
    elif selection==choice:
        print("its win")
    else:
        print("you lose")




