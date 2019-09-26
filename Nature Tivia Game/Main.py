"""
  Main.py - Main will operate as the center script for all imported python files
  Created by: Christopher S Coram
  Created on: 09242019
"""
# import classes from other python files located in directiry
from LevelOne import *

#####################
##### VARIABLES #####
#####################

# ------- CLASS IMPORTS -------
from LevelOne import *

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
  print(top_Layer)
  print(game_Title)
  print(developer)
  print(lower_Layer)

