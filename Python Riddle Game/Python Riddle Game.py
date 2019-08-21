"""
@author: Christopher S Coram
Python Math Game
8-21-2019 4:56PM
"""
#################
#### IMPORTS ####
#################
import math
import numpy

###################
#### VARIABLES ####
###################
# Question
question_one = "I can be liquid or solid, sometimes I bubble and you can find me in every home. What am I?"
question_two = "How many hairs in a rabbits tail?"
question_three = "Three eyes have I, all in a row; when the red one opens, all freeze."
# Answer
answer_one = input("Soap")
answer_two = input("None")
answer_two = input("Traffic Light")
# Display layout
row_one = "************"
row_two = "******"
row_three = "******__________******"
# Character display
display_1 = "T*T"
display_2 = "T*T______T*T"
display_3 = "T*T______T*T______T*T"
# Game loop variable
game_play = True
main_set = True

#######################
#### CLASS HOLDERS ####
#######################

# Level one class
class level_one():
    def __init__(self):
        print("uploading level....")

    def play_one(self):
        while game_play:
            if (answer_one == input("Soap")):
                print("You got it right!")
                print(display_1)
            else:
                print("GAME OVER")
                # End game loop

# Store class data in lvOne object
object_lvOne = level_one()


# Level two class
class level_two():
    def __init__(self):
        print("uploading level....")

    def play_two(self):
        while game_play:
            if (answer_two == input("None")):
                print("You got it right!")
                print(display_2)
            else:
                print("GAME OVER")
                # End game loop


# Store class data in lvOne object
object_lvTwo = level_two()


# Leve3 one class
class level_three():
    def __init__(self):
        print("uploading level....")

    def play_three(self):
        while game_play:
            if (answer_three == input("Traffic Light")):
                print("You got it right!")
                print(display_3)
            else:
                print("GAME OVER")
                # End game loop


# Store class data in lvOne object
object_lvThree = level_three()


# Controls how player moves through levels
class center():
    def center_call(self):
        if(answer_one == input("Soap")):
            print(object_LvOne)
        if(answer_two == input("None")):
            print(object_LvTwo)
        if(answer_three == input("Traffic Light")):
            print(object_LvThree)

###################
#### GAME LOOP ####
###################
while main_set:
    print("INSTRUCTIONS: ")
    print(row_three)
    # calling levels
    print(center_call)
    print(row_one)
