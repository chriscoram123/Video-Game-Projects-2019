"""
  PythonWordGame.py - Python word trivia game for terminal / user input
  Created by: Christopher S Coram
  Created on: 09242019
"""
import sys

#####################
##### VARIABLES #####
#####################
# Scripting practice
# Game layout
bl_Section1 = 0
bl_Section2 = 0
bl_Section3 = 0
# Game questions
question_one = "What color are the clouds?"
question_two = "What color is the grass?"
question_three = "What color is the ocean?"
# Game awnsers / layout
bl_Section1_A = "0000Correct0000"
bl_Section2_A = "0000Correct0000"
bl_Section3_A = "0000Correct0000"

######################
#### GAME CLASSES ####
######################
# game_questions will hold all main game functions
class game_questions():
  
  def level(self):
    print(bl_Section1)
    print(bl_Section2)
    print(bl_Section3)
    print("Instructions: ")
    # Question one if / else statements
    question_One = input("What color are the clouds?")
    if question_One == "white":
      print("Correct")
      print(bl_Section1_A)
      print(bl_Section2)
      print(bl_Section3)
    else:
      print("Wrong, GAME OVER")
      sys.exit()
      
    # Question Two if / else statements
    question_Two = input("What color is the grass?")
    if question_Two == "green":
      print("Correct")
      print(bl_Section1_A)
      print(bl_Section2_A)
      print(bl_Section3)
    else:
      print("Wrong, GAME OVER")
      sys.exit()
      
    # Question three if / else statements
    question_Three = input("What color is the grass?")
    if question_Three == "blue":
      print("Correct")
      print(bl_Section1_A)
      print(bl_Section2_A)
      print(bl_Section3_A)
      print("You Beat the game!")
    else:
      print("Wrong, GAME OVER")
      sys.exit()

game_x = game_questions()

print(game_x.level())
