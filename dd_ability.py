from random import randrange


difficulty = int(input("Enter the DC!: "))

#processing and output

player_roll = randrange(1,21)


print(f"The player has rolled {player_roll} on their D20")

if player_roll >= difficulty:
    print(f"Player was succesful as {player_roll} >= {difficulty}")
else: 
    print(f"The player was not succesful as {player_roll} < {difficulty}")