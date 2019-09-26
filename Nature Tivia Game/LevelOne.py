"""
  LevelOne.py - LevelOne will contain all functions and operations related to questions and user input for
  round one of video game.
  Created by: Christopher S Coram
  Created on: 09242019
"""
import sys

#####################
##### VARIABLES #####
#####################
# Hint variables
hint_One = "HINT: PHOTOgraphy"
hint_Two = "HINT: They're looking for a mate..."
hint_Three = "HINT: I've been asleep for one year lower than the legal drinking age times 10000 years."
hint_Four = "HINT: Knew this since I was four...duh."
hint_Five = "HINT: wow my dad looks like he's going erupt drom anger...."

# Variables that relate to constructing all questions related to round one.
question_One = "What is the name of the process where plants absorb sunlight for energy?" + hint_One
question_Two = "What is the name of the season where animals, both male anf female, look for mates to produce new life?" + hint_Two
question_Three = "How many years have homosapiens walked the earth?" + hint_Three
question_Four = "How many oceans are known in existance on earth?" + hint_Four
question_Five = "What is the name of the proccess of pressurized lava exiting an opening in a volcano." + hint_Five

# Game Score 
rd_Point = 10
maximum_Points = 50   

##########################
##### GAME QUESTIONS #####
##########################
# Class level_One will hold all round one operating features
class q_One:
  def __init__(self):
    # __init__ function for proper class setup.
    print("File running")

 # Def round_Questions will contain all of level one's questions
  def round_Questions(self):
    print("ROUND ONE")
    # input variables will contain round one questions
    input_One = input(question_One)
    # Question one if / else statements
    if input_One == "Photosynthesis":
      print("Correct!")
      print("Player has been awarded " + str(rd_Point))
    else: # If player enters in wrong answer a second time
      print("Wrong! GAME OVER")
      sys.exit()
    
    input_Two = input(question_Two)
    # Question two if / else statements
    if input_Two == "Mating Season":
      print("Correct!")
      print("Player has been awarded " + str(rd_Point))
    else: # If player enters in wrong answer a second time
      print("Wrong! GAME OVER")
      sys.exit()
    
    input_Three = input(question_Three)
    # Question three if / else statements
    if input_Three == "20000":
      print("Correct!")
      print("Player has been awarded " + str(rd_Point))
    elif input_Three == "Twenty Thousand Years": # Gives player a second chance
      print("Correct!")
      print("Player has been awarded " + str(rd_Point))
    else: # If player enters in wrong answer a second time
      print("Wrong! GAME OVER")
      sys.exit()
    
    input_Four = input(question_Four)
    # Question four if / else statements
    if input_Four == "Four":
      print("Correct!")
      print("Player has been awarded " + str(rd_Point))
    elif input_Four == "4": # Gives player a second chance
      print("Correct!")
      print("Player has been awarded " + str(rd_Point))
    else: # If player enters in wrong answer a second time
      print("Wrong! GAME OVER")
      sys.exit()

    input_Five = input(question_Five)
    # Question five if / else statements
    if input_Five == "Eruption":
      print("Correct!")
      print("Player has been awarded " + str(rd_Point))
    else: # If player enters in wrong answer a second time
      print("Wrong! GAME OVER")
      sys.exit()

    # Awards player with a total of 50 points
    print("Congratz! you beat round one and earned a total of " + str(maximum_Points) + "points")
