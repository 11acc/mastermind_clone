
#*************************************************************************************/
# NAME: Alejandro Gutierrez Acosta, Lourdes Mariana Reyes Alegria, Sana Ala Y. Barakat
# ORGN: BS Computer Science & Artificial Intelligence / Algorithms & Data Structures
# PROJ: Mastermind+
# FILE: code_search.py
# DATE: Nov 27th 2022
#*************************************************************************************/

from graphics import *
from button import *
import random as rand

def generate_buttons(win, dimensions):
  # Runtime complexity:
  #   Worst-case    : O(n^2)
  #   Average-case  : O(n^2)
  # generate_buttons() generates as many buttons as the dimensions
  #   of the board have been decided for, in this case 6x6
  row, col = int(dimensions[0]), int(dimensions[-1])
  y = 127
  w, h = 48, 50
  buttons = []

  for r_sqr in range(row):
    x = 70
    for c_sqr in range(col):
      # While generating the buttons, store in an array along side it
      # the position of the button so that we can identify it later on
      temp = [(6 * r_sqr) + c_sqr, Button(win, Point(x, y), w, h, '')]
      temp[1].activate()
      buttons.append(temp)
      x += w + 5
    y += h + 5

  return buttons


def generate_board(dimensions):
  # Runtime complexity:
  #   Worst-case    : O(n)
  #   Average-case  : O(n)
  # generate_board() generates a flat 1d array for the 36 buttons
  #   using list comprehension
  return [[i, 0] for i in range(int(dimensions[0]) * int(dimensions[-1]))]


def rand_colour():
  # Runtime complexity:
  #   Worst-case    : O(n)
  #   Average-case  : O(n)
  # rand_colour() return's a random colour from the list below
  return rand.choice(["red", "blue", "green", "yellow", "orange", "purple"])


def hide_pins(win, search_code_l, button_list):
  # Runtime complexity:
  #   Worst-case    : O(n)
  #   Average-case  : O(n)
  # hide_pins() prompts the user to select the tiles in the set
  #   of buttons, or board, to hide 4 pins. Then thanks to the 
  #   location of the buttons alongside the button objects, we
  #   isolte their location and return them for later use
  pin_location = []
  while len(pin_location) < search_code_l:
    pt = win.getMouse()
    for b in range(len(button_list)):
      if button_list[b][1].clicked(pt):
        button_list[b][1].rect.setFill(rand_colour())
        loc = button_list[b][0]
        pin_location.append(loc)
        break

  return pin_location


def add_pins_to_board(flatten_list, pin_location):
  # Runtime complexity:
  #   Worst-case    : O(n)
  #   Average-case  : O(n)
  # add_pins_to_board() adds the location of the pins to the flat
  #   list of 36 'buttons'
  for i in pin_location:
    flatten_list[i][1] = 1
  return flatten_list


def identify_flat_pins(pins, dimensions):
  # Runtime complexity:
  #   Worst-case    : O(n^2)
  #   Average-case  : O(n^2)
  # identify_flat_pins() identifies which location would the pins be
  #   in a 2d array from the 1d version of the array
  found_pins = []
  row_l = int(dimensions[0])

  for pin in pins:
    row, col = -1, -1
    counter = 0
    temp = pin
    if temp < row_l:
      row = 0
      col = temp
    else:
      while temp > row_l:
        temp -= row_l
        counter += 1
      row = counter
      col = temp
    found_pins.append([row, col])

  return found_pins


def linear_search(flat_search_board):
  # Runtime complexity:
  #   Worst-case    : O(n^2)
  #   Average-case  : O(n^2)
  # linear_search() searching method to find the hidden pins

  identified_pins = []
  for tile in flat_search_board:
    if tile[1] == 1:
      identified_pins.append(tile[0])

  return identified_pins
