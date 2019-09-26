"""
  LevelTwo.py - LevelTwo will contain all functions and operations related to questions and user input.
  Created by: Christopher S Coram
  Created on: 09242019
"""
import sys

#####################
##### VARIABLES #####
#####################
# Hint variables
hint_One = "HINT: Almost the same amount of days in the year..."
hint_Two = "HINT: Sir, you were driving 15 miles faster than the 50 mile speed limit..."
hint_Three = "HINT: Miami sounds nice when it gets this cold..."
hint_Four = "HINT: What species grows fur and warm blooded?..."
hint_Five = "HINT: Don't even need to give you hint on this one... "

# Variables that relate to constructing all questions related to round one.
question_One = "How many teeth does a great white shark have?" + hint_One
question_Two = "How fast can a chettah run?" + hint_Two
question_Three = "What time of the year do birds fly south?" + hint_Three
question_Four = "What animal species do human beings belong to?" + hint_Four
question_Five = "Who's man's best friend?" + hint_Five

# Game Score 
rd_Point = 10
maximum_Points = 50


##########################
##### GAME QUESTIONS #####
##########################
# Class level_One will hold all round one operating features
class q_Two:
  def __init__(self):
    # __init__ function for proper class setup.
    print("File running")

 # Def round_Questions will contain all of level one's questions
  def round_Questions_Two(self):
    print("ROUND TWO")
    # input variables will contain round one questions
    input_One = input(question_One)
    # Question one if / else statements
    if input_One == "300":
      print("Correct!")
      print("Player has been awarded" + str(rd_Point))
    elif input_One == "Three Hundred Teeth": # Gives player a second chance
      print("Correct!")
      print("Player has been awarded" + str(rd_Point))
    else: # If player enters in wrong answer a second time
      print("Wrong! GAME OVER")
      sys.exit()
    
    input_Two = input(question_Two)
    # Question two if / else statements
    if input_Two == "65":
      print("Correct!")
      print("Player has been awarded" + str(rd_Point))
    elif input_Two == "Sixty five miles per hour": # Gives player a second chance
      print("Correct!")
      print("Player has been awarded" + str(rd_Point))
    elif input_Two == "65 miles per hour": # Gives player a second chance
      print("Correct!")
      print("Player has been awarded" + str(rd_Point))
    else: # If player enters in wrong answer a second time
      print("Wrong! GAME OVER")
      sys.exit()
    
    input_Three = input(question_Three)
    # Question three if / else statements
    if input_Three == "South":
      print("Correct!")
      print("Player has been awarded" + str(rd_Point))
    else: # If player enters in wrong answer a second time
      print("Wrong! GAME OVER")
      sys.exit()
    
    input_Four = input(question_Four)
    # Question four if / else statements
    if input_Four == "Mammals":
      print("Correct!")
      print("Player has been awarded" + str(rd_Point))
    else: # If player enters in wrong answer a second time
      print("Wrong! GAME OVER")
      sys.exit()

    input_Five = input(question_Five)
    # Question five if / else statements
    if input_Five == "Dog":
      print("Correct!")
      print("Player has been awarded" + str(rd_Point))
    elif input_Five == "": # If player enters in anything else besides the right answer
      print("you get one more try! Here is a hint")
      print(hint_Five)
    elif input_Two == "Dogs": # Gives player a second chance
      print("Correct!")
      print("Player has been awarded" + str(rd_Point))
    else: # If player enters in wrong answer a second time
      print("Wrong! GAME OVER")
      sys.exit()
  
    # Awards player with a total of 50 points
    print("Congratz! you beat round two and earned a total of " + str(maximum_Points) + "points")
