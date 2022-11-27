
#*************************************************************************************/
# NAME: Alejandro Gutierrez Acosta, Lourdes Mariana Reyes Alegria, Sana Ala Y. Barakat
# ORGN: BS Computer Science & Artificial Intelligence / Algorithms & Data Structures
# PROJ: Mastermind+
# FILE: code_breaker.py
# DATE: Nov 27th 2022
#*************************************************************************************/

from graphics import *
from queue_stack import *
import random as rand

def generate_code(colours_map, code_l):
  # Runtime complexity:
  #   Worst-case    : O(n)
  #   Average-case  : O(n)
  # generate_code() generates a random set of numbers
  #   from the game's set of colours
  code = []
  k = 0
  while k < code_l:
    choice = rand.choice(colours_map)
    if choice not in code:
      code.append(choice)
      k += 1
  return code


def generate_guess(win, code_l, y_cord, buttons, colours_map):
  # Runtime complexity:
  #   Worst-case    : O(n log n)
  #   Average-case  : O(n log n)
  # generate_guess() prompts the user to click on the visual pins
  #   set in the game winodow. A guess code is generated.

  # We use a stack to store the user's pin choices in order to have
  #   an undo funciton, correcting the user's mistake if it's the case
  guess_stack = Stack()
  red = buttons[0]
  blue = buttons[1]
  green = buttons[2]
  yellow = buttons[3]
  orange = buttons[4]
  purple = buttons[5]
  undo = buttons[6]
  x_cord = 92
  size = 14.5

  # Loop until 4 pins have been chosen
  while guess_stack.stack_size < code_l:
    button_clicked = False
    pt = win.getMouse()
    if red.clicked(pt):
      print("red pin selected")
      guess_stack.push(str(colours_map[0]))
      button_clicked = True
    elif blue.clicked(pt):
      print("blue pin selected")
      guess_stack.push(str(colours_map[1]))
      button_clicked = True
    elif green.clicked(pt):
      print("green pin selected")
      guess_stack.push(str(colours_map[2]))
      button_clicked = True
    elif yellow.clicked(pt):
      print("yellow pin selected")
      guess_stack.push(str(colours_map[3]))
      button_clicked = True
    elif orange.clicked(pt):
      print("orange pin selected")
      guess_stack.push(str(colours_map[4]))
      button_clicked = True
    elif purple.clicked(pt):
      print("purple pin selected")
      guess_stack.push(str(colours_map[5]))
      button_clicked = True
    elif undo.clicked(pt):
      # If the undo button is clicked, first check that its not
      #   done with no prior pin selected
      if guess_stack.stack_size >= 1:
        guess_stack.pop()
        x_cord -= 37
        # Call a function to display in the window the pin being
        #  selected for the guess code
        indiv_pin_undo(win, guess_stack, x_cord, y_cord, size)
    
    if button_clicked:
      # Call a function to display in the window the pin being
      #  selected for the guess code
      indiv_pin_change(win, guess_stack, x_cord, y_cord, size)
      x_cord += 37
    
  return guess_stack


def check_guess(code, guess):
  # Runtime complexity:
  #   Worst-case    : O(n^2)
  #   Average-case  : O(n^2)
  # generate_guess() prompts the user to click on the visual pins
  #   set in the game winodow. A guess code is generated.

  # Rules:
  #   if colour + position = black peg  ● = 1
  #   if colour + !position = white peg  ○ = 2
  #   if !colour + !position = nothing ⏻ = 3
  perfect_guess = 0
  feedback_pegs = []
  
  # Loop accross each pin in the code and guess, since we can hint
  #  at the position being incorrect but the pin being correct
  #  a loop for each pin of code is necessary
  for c in range(len(code)):
    for g in range(len(guess.stack_list)):
      if guess.stack_list[g].value == code[c]:
        if g == c:
          feedback_pegs.append(' ● ')
          perfect_guess += 1
          break
        else:
          feedback_pegs.append(' ○ ')
          break

  for _ in range(len(code) - len(feedback_pegs)):
    feedback_pegs.append(' ⏻ ')

  rand.shuffle(feedback_pegs)
  print(feedback_pegs)

  # Return if the user has correctly obtained the code
  if perfect_guess == len(code):
    return True, feedback_pegs
  return False, feedback_pegs


def indiv_pin_change(win, guess_stack, x_cord, y_coor, size):
  # Runtime complexity:
  #   Worst-case    : O(1)
  #   Average-case  : O(1)
  # indiv_pin_change() simply displays in the window each of the
  #  user's pin choices
  pin = Circle(Point(x_cord, y_coor), size)
  pin.setFill(guess_stack.top.value)
  pin.draw(win)


def indiv_pin_undo(win, guess_stack, x_cord, y_coor, size):
  # Runtime complexity:
  #   Worst-case    : O(1)
  #   Average-case  : O(1)
  # indiv_pin_undo() deletes the unwanted pin choice by the user
  pin = Circle(Point(x_cord, y_coor), size)
  pin.setFill("white")
  pin.draw(win)


def clues_color(win, x_coor, y_coor, size, cluesList):
  # Runtime complexity:
  #   Worst-case    : O(n)
  #   Average-case  : O(n)
  # clues_color() displays the white, black and grey pins according
  #  to their guess
  pins = []
  pin = Circle(Point(x_coor, y_coor), size)
  pin2 = Circle(Point(x_coor + 25, y_coor), size)
  pin3 = Circle(Point(x_coor + 50, y_coor), size)
  pin4 = Circle(Point(x_coor + 75, y_coor), size)
  pins.append(pin)
  pins.append(pin2)
  pins.append(pin3)
  pins.append(pin4)
  num = 0
  for i in pins:
    print('this for loop is running', cluesList[num])
    if cluesList[num] == ' ● ':
      print('blackpin')
      i.setFill("black")
    elif cluesList[num] == ' ○ ':
      print('whitepin')
      i.setFill("white")
    elif cluesList[num] == ' ⏻ ':
      print('nothing')
      i.setFill("grey")
    num += 1
    i.draw(win)