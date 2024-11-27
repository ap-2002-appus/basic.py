'''
Authour:Ibin Siby
Discription:python program to create and modify a list of favorite games. You will:

1.Create a list of three favorite games.
2.Ask the user to add a new game to the list.
3.Display the updated list of games.
4.Ask the user to remove one game from the list.
5.Display the final list of games.

'''



games=['Minecraft', 'Subway surfer', 'Dr driving']
print("Current list of games:",games)
new_game=input("Enter a game to add:")
games.append(new_game)
print("Updated list of games:",games)
game_remove=input("Enter a game to remove:")
games.remove(game_remove)
print("Final list of games:",games)'