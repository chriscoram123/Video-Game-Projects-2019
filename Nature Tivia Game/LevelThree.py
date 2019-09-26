"""
  LevelThree.py - LevelThree will contain all functions and operations related to questions and user input.
  Created by: Christopher S Coram
  Created on: 09242019
"""
import sys

#####################
##### VARIABLES #####
#####################
# Hint variables
hint_One = "HINT: ..."
hint_Two = "HINT:  ..."
hint_Three = "HINT: ..."
hint_Four = "HINT: ..."
hint_Five = "HINT: ... "

# Variables that relate to constructing all questions related to round one.
question_One = "How many tenticles does a squid have?..." + hint_One
question_Two = "How far can a bald eagle see something like a rabbit?" + hint_Two
question_Three = "Do male sea horses give birth?" + hint_Three
question_Four = "Whats the most venomous spider in the world?" + hint_Four
question_Five = "Are black bears dangerous" + hint_Five

# Game Score 
rd_Point = 10
maximum_Points = 50


##########################
##### GAME QUESTIONS #####
##########################
# Class level_One will hold all round one operating features
class q_Three:
  def __init__(self):
    # __init__ function for proper class setup.
    print("File running")

 # Def round_Questions will contain all of level one's questions
  def round_Questions_Three(self):
    print("ROUND THREE")
    print("NO HINTS!")
    # input variables will contain round one questions
    input_One = input(question_One)
    # Question one if / else statements
    if input_One == "two":
      print("Correct!")
      print("Player has been awarded" + str(rd_Point))
    elif input_One == "2": # Gives player a second chance
      print("Correct!")
      print("Player has been awarded" + str(rd_Point))
    else: # If player enters in wrong answer a second time
      print("Wrong! GAME OVER")
      sys.exit()
    
    input_Two = input(question_Two)
    # Question two if / else statements
    if input_Two == "three miles":
      print("Correct!")
      print("Player has been awarded" + str(rd_Point))
    elif input_Two == "3 miles": # Gives player a second chance
      print("Correct!")
      print("Player has been awarded" + str(rd_Point))
    else: # If player enters in wrong answer a second time
      print("Wrong! GAME OVER")
      sys.exit()
    
    input_Three = input(question_Three)
    # Question three if / else statements
    if input_Three == "No":
      print("Correct!")
      print("Player has been awarded" + str(rd_Point))
    else: # If player enters in wrong answer a second time
      print("Wrong! GAME OVER")
      sys.exit()
    
    input_Four = input(question_Four)
    # Question four if / else statements
    if input_Four == "Atrax Robustus":
      print("Correct!")
      print("Player has been awarded" + str(rd_Point))
    else: # If player enters in wrong answer a second time
      print("Wrong! GAME OVER")
      sys.exit()

    input_Five = input(question_Five)
    # Question five if / else statements
    if input_Five == "No":
      print("Correct!")
      print("Player has been awarded" + str(rd_Point))
    else: # If player enters in wrong answer a second time
      print("Wrong! GAME OVER")
      sys.exit()
    
    # Awards player with a total of 50 points
    print("Congratz! you beat round three and earned a total of " + str(maximum_Points) + "points")
