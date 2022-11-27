
#*************************************************************************************/
# NAME: Alejandro Gutierrez Acosta, Lourdes Mariana Reyes Alegria, Sana Ala Y. Barakat
# ORGN: BS Computer Science & Artificial Intelligence / Algorithms & Data Structures
# PROJ: Mastermind+
# FILE: main.py
# DATE: Nov 27th 2022
#*************************************************************************************/

from graphics import *
from clear import clear
from innit_vars import innit_vars

from intro import intro
from instructions import instructions
from breaker import breaker
from search import search
from sorting import sorting_master

###--- ··· ---###

def main():
  # Runtime complexity:
  #   Worst-case    : O(1)
  #   Average-case  : O(1)
  # main() is the primary function of the program, calling all 
  #   necessary parts of the code in order for the game to function

  # In order to maintain a cohesive base global variables, we
  #   save them in a separate file and call a function returning
  #   them in an array
  innitVars = innit_vars()

  # Other variables needed for the main menu
  name = ""
  intro_output = -1
  win_condition = None
  
  # Using the graphics.py library to handle the visual aspects of
  #   the game, we create the main menu screen
  win = GraphWin("GameIntro", 400, 566)
  
  # We call another function which draws the necessay visuals for the
  #   main menu, and returns the user's name and desired game mode.
  intro_output, name = intro(win)

  if intro_output == 0:
    # Clear the main menu window and show the instructions window
    clear(win)
    inst = instructions(win, intro_output)
    # Once the instructions screen is finished, clear the window
    #   again to give way to the following game mode
    if inst == 0:
      clear(win)
    # Call the game mode funciton
    breaker(win, innitVars)
  elif intro_output == 1:
    # Clear main menu
    clear(win)
    inst = instructions(win, intro_output)
    if inst == 0:
      clear(win)
    # Call the game mode funciton
    search(win, innitVars)
  elif intro_output == 2:
    # Clear main menu
    clear(win)
    inst = instructions(win, intro_output)
    if inst == 0:
      clear(win)
    # Call the game mode funciton
    sorting_master(win, innitVars)

  # We close the program when the user is done playing one of the games
  win.close()

###--- ··· ---###

main()
