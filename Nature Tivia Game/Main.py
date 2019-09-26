"""
  Main.py - Main will operate as the center script for all imported python files
  Created by: Christopher S Coram
  Created on: 09242019
"""
# ------- CLASS IMPORTS -------
# import classes from other python files located in directiry
from LevelOne import *
from LevelTwo import *
from LevelThree import *


#####################
##### VARIABLES #####
#####################
# Imported classes
classOne = q_One()
classTwo = q_Two()
classThree = q_Three()

# Main title display 
top_Layer =  "-----------------------"
lower_Layer = "----------------------"
game_Title = "NATURE TRIVA GAME"
developer = "by Christopher S Coram"

# Loop variable
game_Running = True


################
##### GAME #####
################
# Video game title display
while game_Running:
  print(top_Layer)
  print(game_Title)
  print(developer)
  print("INSTRUCTIONS: When entering answers do not space out the first letter from the last letter in HINT.")
  print("Also, always capitalize the first letter of your answer.")
  print(lower_Layer)

  # Running LevelOne questions
  classOne.round_Questions()
  print(lower_Layer)
  # Running LevelTwo questions
  classTwo.round_Questions_Two()
  print(lower_Layer)
  # Running LevelThree questions
  classThree.round_Questions_Three()
  print(lower_Layer)

  # Decision if / else statement
  if input("You gained a total of 150 points! Now that the game is finished, would you like to exit the game or play again?(yes/no)") == "Yes":
    print("Continue loop")
  elif input("You gained a total of 150 points! Now that the game is finished, would you like to exit the game or play again?(yes/no)") == "yes":
    print("Continue loop")
  elif input("You gained a total of 150 points! Now that the game is finished, would you like to exit the game or play again?(yes/no)") == "No":
    sys.exit()
  elif input("You gained a total of 150 points! Now that the game is finished, would you like to exit the game or play again?(yes/no)") == "no":
    sys.exit()
    
