
#*************************************************************************************/
# NAME: Alejandro Gutierrez Acosta, Lourdes Mariana Reyes Alegria, Sana Ala Y. Barakat
# ORGN: BS Computer Science & Artificial Intelligence / Algorithms & Data Structures
# PROJ: Mastermind+
# FILE: breaker.py
# DATE: Nov 27th 2022
#*************************************************************************************/

from graphics import *
from button import *

from code_breaker import generate_code
from code_breaker import generate_guess
from code_breaker import check_guess
from code_breaker import clues_color
from code_breaker import clear

def breaker(win, innitVars):
  # Runtime complexity:
  #   Worst-case    : O(n)
  #   Average-case  : O(n)
  # Main function for the breaker game, displays all the necessary
  #   graphics components and calls the necessary functions to make
  #   the breaker game function

  # Create the window for the game
  background = Image(Point(200, 283), "pictures/Breaker.gif")
  background.draw(win)

  # 1.1 create buttons
  red_btn = Button(win, Point(107, 482), 14, 14, '')
  blue_btn = Button(win, Point(144, 482), 14, 14, '')
  green_btn = Button(win, Point(182, 482), 14, 14, '')
  yellow_btn = Button(win, Point(219, 482), 14, 14, '')
  orange_btn = Button(win, Point(256, 482), 14, 14, '')
  purple_btn = Button(win, Point(293, 482), 14, 14, '')
  undo_btn = Button(win, Point(200, 530), 50, 16, 'Undo')

  buttons = [red_btn, blue_btn, green_btn, yellow_btn, orange_btn, purple_btn, undo_btn]

  # 1.2 activate buttons
  red_btn.activate()
  blue_btn.activate()
  green_btn.activate()
  yellow_btn.activate()
  orange_btn.activate()
  purple_btn.activate()
  undo_btn.activate()

  # 2.1 create pins
  redpin = Circle(Point(107, 482), 14)
  bluepin = Circle(Point(143, 482), 14)
  greenpin = Circle(Point(181, 482), 14)
  yellowpin = Circle(Point(218, 482), 14)
  orangepin = Circle(Point(256, 482), 14)
  purplepin = Circle(Point(293, 482), 14)

  # 2.2 colour pins
  redpin.setFill("red")
  bluepin.setFill("blue")
  greenpin.setFill("green")
  yellowpin.setFill("yellow")
  orangepin.setFill("orange")
  purplepin.setFill("purple")

  # 2.3 print the pins
  redpin.draw(win)
  bluepin.draw(win)
  greenpin.draw(win)
  yellowpin.draw(win)
  orangepin.draw(win)
  purplepin.draw(win)
  
  # Some global variables needed
  attempts = innitVars[0]
  code_l = innitVars[1]
  colours_map = innitVars[2]

  # Call function to generate code
  code = generate_code(colours_map, code_l)
  print(f"code: {code}")

  win_condition = None
  # Base y-coordinate for the location of the buttons
  y_cord = 27.7

  # Loop prompting the user to guess 'attempts' number of times
  for i in range(attempts):
    # Call a function to generate a guess according to innit variables
    guess = generate_guess(win, code_l, y_cord, buttons, colours_map)
    # Check for win condition
    win_condition, cluesList = check_guess(code, guess)
    # To display clues
    clues_color(win, 238, y_cord, 10, cluesList)
    
    # Check if user won, if so show winning screen
    if win_condition:
      print("Congratulations you won in " + str(i + 1) + " attempts!")
      clear(win)
      background = Image(Point(200, 283), "pictures/congrats.gif")
      background.draw(win)
      win.getMouse()
      break
    y_cord += 40

  # If user lost, show game over screen
  if win_condition == False:
    #color_click_change(win, 92, y_num, 14.5, guess)
    print("Sorry you ran out of attempts! Better luck next time.")
    clear(win)
    background = Image(Point(200, 283), "pictures/oops.gif")
    background.draw(win)
    win.getMouse()