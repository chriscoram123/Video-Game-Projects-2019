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

# Main title display 
top_Layer =  "1001000100100010001000"
lower_Layer = "001001000100010001001"
game_Title = "NATURE TRIVA GAME"
developer = "by Christopher S Coram"

# Loop variable
game_Running = True


######################
##### WHILE LOOP #####
######################
while game_Running:
  # Video game title display
  print(top_Layer)
  print(game_Title)
  print(developer)
  print(lower_Layer)

