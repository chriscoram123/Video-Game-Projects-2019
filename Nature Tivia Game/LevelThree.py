"""
  LevelThree.py - LevelThree will contain all functions and operations related to questions and user input.
  Created by: Christopher S Coram
  Created on: 09242019
"""
import sys

#####################
##### VARIABLES #####
#####################
# Variables that relate to constructing all questions related to round one.
question_One = ""
question_Two = ""
question_Three = ""
question_Four = ""
question_Five = ""

# Hint variables
hint_One = ""
hint_Two = ""
hint_Three = ""
hint_Four = ""
hint_Five = ""
# Game Score 
rd_Point = 10
maximum_Points = 50


##########################
##### GAME QUESTIONS #####
##########################
# Class level_One will hold all round one operating features
class level_Three:
 # Def round_Questions will contain all of level one's questions
  def round_Questions(self):
    print("Instructions: ")
    # input variables will contain round one questions
    input_One = input(question_One)
    # Question one if / else statements
    if input_One == "---":
      print("Correct!")
      print("Player has been awarded" + str(rd_Point))
    elif input_One == "": # If player enters in anything else besides the right answer
         print("you get one more try! Here is a hint") 
         print(hint_One)
    elif input_One == "---": # Gives player a second chance
      print("Correct!")
      print("Player has been awarded" + str(rd_Point))
    else: # If player enters in wrong answer a second time
      print("Wrong! GAME OVER")
      sys.exit()
    
    input_Two = input(question_Two)
    # Question two if / else statements
    if input_Two == "---":
      print("Correct!")
      print("Player has been awarded" + str(rd_Point))
    elif input_Two == "": # If player enters in anything else besides the right answer
      print("you get one more try! Here is a hint")
      print(hint_Two)
    elif input_Two == "---": # Gives player a second chance
      print("Correct!")
      print("Player has been awarded" + str(rd_Point))
    else: # If player enters in wrong answer a second time
      print("Wrong! GAME OVER")
      sys.exit()
    
    input_Three = input(question_Three)
    # Question three if / else statements
    if input_Three == "---":
      print("Correct!")
      print("Player has been awarded" + str(rd_Point))
    elif input_Three == "": # If player enters in anything else besides the right answer
      print("you get one more try! Here is a hint")
      print(hint_Three)
    elif input_Three == "---": # Gives player a second chance
      print("Correct!")
      print("Player has been awarded" + str(rd_Point))
    else: # If player enters in wrong answer a second time
      print("Wrong! GAME OVER")
      sys.exit()
    
    input_Four = input(question_Four)
    # Question four if / else statements
    if input_Four == "---":
      print("Correct!")
      print("Player has been awarded" + str(rd_Point))
    elif input_Four == "": # If player enters in anything else besides the right answer
      print("you get one more try! Here is a hint")
      print(hint_Four)
    elif input_Four == "---": # Gives player a second chance
      print("Correct!")
      print("Player has been awarded" + str(rd_Point))
    else: # If player enters in wrong answer a second time
      print("Wrong! GAME OVER")
      sys.exit()

    input_Five = input(question_Five)
    # Question five if / else statements
    if input_Five == "---":
      print("Correct!")
      print("Player has been awarded" + str(rd_Point))
    elif input_Five == "": # If player enters in anything else besides the right answer
      print("you get one more try! Here is a hint")
      print(hint_Five)
    elif input_Two == "---": # Gives player a second chance
      print("Correct!")
      print("Player has been awarded" + str(rd_Point))
    else: # If player enters in wrong answer a second time
      print("Wrong! GAME OVER")
      sys.exit()

# Game_x will contain level_One class
game_x = level_Three
