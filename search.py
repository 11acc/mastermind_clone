
#*************************************************************************************/
# NAME: Alejandro Gutierrez Acosta, Lourdes Mariana Reyes Alegria, Sana Ala Y. Barakat
# ORGN: BS Computer Science & Artificial Intelligence / Algorithms & Data Structures
# PROJ: Mastermind+
# FILE: search.py
# DATE: Nov 27th 2022
#*************************************************************************************/

from graphics import *
from button import *

from code_search import generate_board
from code_search import generate_buttons
from code_search import hide_pins
from code_search import add_pins_to_board
from code_search import linear_search
from code_search import identify_flat_pins


def search(win, innitVars):
  # Runtime complexity:
  #   Worst-case    : O(n)
  #   Average-case  : O(n)
  # Main function for the search game, displays all the necessary
  #   graphics components and calls the necessary functions to make
  #   the search game function

  # Create window for the game
  background = Image(Point(200, 283), "pictures/search_master.gif")
  background.draw(win)

  # Global vars
  search_code_l = innitVars[3]
  dimensions = innitVars[4]
  pending_continue = True

  # Generate the board
  flatten_list = generate_board(dimensions)
  button_list = generate_buttons(win, dimensions)
  
  # Ask user to hide the pins and add them to board
  pin_location = hide_pins(win, search_code_l, button_list)
  
  flatten_list = add_pins_to_board(flatten_list, pin_location)
  
  comp = Text(Point(203, 450), "Computer will now search for the hidden pins!")
  comp.setSize(10)
  comp.setStyle("bold")
  comp.setTextColor("white")
  comp.draw(win)
  
  cont_btn = Button(win, Point(203, 540), 100, 25, 'Continue')
  cont_btn.activate()
  
  while pending_continue:
    pt = win.getMouse()
    if cont_btn.clicked(pt):
      pending_continue = False
  
  # Call the searching algorithm for it to search for the hidden
  #   pins in the board
  flat_list = linear_search(flatten_list)
  found_pins = identify_flat_pins(flat_list, dimensions)

  # Display the found pins from the searching algorithm
  str_found = ""
  for p in found_pins:
    str_found += str(p) + "   "
  
  found = Text(Point(203, 480), "Pins found at locations [row, column]:")
  found.setSize(10)
  found.setStyle("bold")
  found.setTextColor("white")
  found.draw(win)
  
  loc = Text(Point(203, 505), str_found)
  loc.setSize(10)
  loc.setStyle("bold")
  loc.setTextColor("white")
  loc.draw(win)

  win.getMouse()