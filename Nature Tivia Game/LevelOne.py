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
# Variables that relate to constructing all questions related to round one.
question_One = "What is the name of the process where plants absorb sunlight for energy?"
question_Two = "What is the name of the season where animals, both male anf female, look for mates to produce new life?"
question_Three = "How many years have homosapiens walked the earth?"
question_Four = "How many oceans are known in existance on earth?"
question_Five = "What is the name of the proccess of pressurized lava exiting an opening in a volcano."

# Hint variables

hint_One = "PHOTOgraphy"
hint_Two = "They're looking for a mate..."
hint_Three = "I've been asleep for one year lower than the legal drinking age times 10000 years."
hint_Four = "Knew this since I was four, duh."
hint_Five = "who my dad looks like he's going erupt drom anger...."
# Game Score 
rd_Point = 10
maximum_Points = 50

# Class level_One will hold all round one operating features
class level_One:
 # Def round_Questions will contain all of level one's questions
  def round_Questions(self):
    print("Instructions: ")
    # input variables will contain round one questions
    input_One = input(question_One)
    # Question one if / else statements
    if input_One == "Photosynthesis":
      print("Correct!")
      print("Player has been awarded" + str(rd_Point))
    elif input_One == "": # If player enters in anything else besides the right answer
         print("you get one more try! Here is a hint") 
         print(hint_One)
    elif input_One == "Photosynthesis": # Gives player a second chance
      print("Correct!")
      print("Player has been awarded" + str(rd_Point))
    else: # If player enters in wrong answer a second time
      print("Wrong! GAME OVER")
      sys.exit()
    
    input_Two = input(question_Two)
    # Question two if / else statements
    if input_Two == "Mating Season":
      print("Correct!")
      print("Player has been awarded" + str(rd_Point))
    elif input_Two == "": # If player enters in anything else besides the right answer
      print("you get one more try! Here is a hint")
      print(hint_Two)
    elif input_Two == "Mating Season": # Gives player a second chance
      print("Correct!")
      print("Player has been awarded" + str(rd_Point))
    else: # If player enters in wrong answer a second time
      print("Wrong! GAME OVER")
      sys.exit()
    
    input_Three = input(question_Three)
    # Question three if / else statements
    if input_Three == "20000":
      print("Correct!")
      print("Player has been awarded" + str(rd_Point))
    elif input_Three == "": # If player enters in anything else besides the right answer
      print("you get one more try! Here is a hint")
      print(hint_Three)
    elif input_Three == "20000": # Gives player a second chance
      print("Correct!")
      print("Player has been awarded" + str(rd_Point))
    else: # If player enters in wrong answer a second time
      print("Wrong! GAME OVER")
      sys.exit()
    
    input_Four = input(question_Four)
    # Question four if / else statements
    if input_Four == "Blue":
      print("Correct!")
      print("Player has been awarded" + str(rd_Point))
    elif input_Four == "": # If player enters in anything else besides the right answer
      print("you get one more try! Here is a hint")
      print(hint_Four)
    elif input_Four == "Blue": # Gives player a second chance
      print("Correct!")
      print("Player has been awarded" + str(rd_Point))
    else: # If player enters in wrong answer a second time
      print("Wrong! GAME OVER")
      sys.exit()

    input_Five = input(question_Five)
    # Question five if / else statements
    if input_Five == "Four":
      print("Correct!")
      print("Player has been awarded" + str(rd_Point))
    elif input_Five == "": # If player enters in anything else besides the right answer
      print("you get one more try! Here is a hint")
      print(hint_Five)
    elif input_Two == "Four": # Gives player a second chance
      print("Correct!")
      print("Player has been awarded" + str(rd_Point))
    else: # If player enters in wrong answer a second time
      print("Wrong! GAME OVER")
      sys.exit()

# Game_x will contain level_One class
game_x = level_One