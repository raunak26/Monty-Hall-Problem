# MontyHallProblem.py
# Raunak Anand
# Simulation of the Monty Hall Problem
# Calculating probability
# based on whether player switches doors or not
# 

import random

number_games = input("Number of games to play: ") # user input 

try:
    number_games == int(number_games) # check if input is an integer 
    if int(number_games) <= 0: # program will run
                               # only if input is a positive integer
        print("Please enter a positive integer")
        exit() 

except:
    print("Please enter a positive integer")
    exit()


def montynever(): # player never changes doors 
    player_choice = random.randint(1,3) # player's choice
    valuable_prize = random.randint(1,3) # prize behind one of the doors
    doors = [1, 2, 3]
    doors.remove(valuable_prize) # remove door that has prize
    if player_choice != valuable_prize:
        doors.remove(player_choice)
    door_opened = random.choice(doors)
    if player_choice == valuable_prize:
        return True # player wins 
    else:
        return False

def montyalways(): # player always changes doors 
    player_choice = random.randint(1,3) # player's choice 
    valuable_prize = random.randint(1,3) # prize behind one of the doors
    doors = [1, 2, 3]
    doors.remove(valuable_prize) # remove doors that has prize
    if player_choice != valuable_prize:
        doors.remove(player_choice)
    door_opened = random.choice(doors)
    change_door = [1, 2, 3] # player switches doors
    change_door.remove(player_choice)
    change_door.remove(door_opened)
    player_finalchoice = change_door[0]
    if player_finalchoice == valuable_prize:
        return True # player wins 
    else:
        return False

def main():
    nwin = 0 # wins on never switching doors
    awin = 0 # wins on always switching doors
    for i in range(int(number_games)): 
        if montynever():
            nwin = nwin + 1
        if montyalways():
            awin = awin + 1
        i = i + 1
    switching_wins = int(awin)/int(number_games) # probability on winning on switching
    noswitching_wins = int(nwin)/int(number_games) # probability on winning in not switching
    print("Out of",number_games,"games:")
    print("Always switching wins:",switching_wins,"(",awin,"games)")
    print("Never switching wins:",noswitching_wins,"(",nwin,"games)")

main()



            
            
