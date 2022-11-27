from graphics import *
from button import *
from error import error

from code_search import generate_board
from code_search import generate_buttons
from code_search import hide_pins
from code_search import add_pins_to_board
from code_search import linear_search
from code_search import identify_flat_pins
#from code_search import unflatten


def search(win, innitVars):
  background = Image(Point(200, 283), "pictures/search_master.gif")
  background.draw(win)

  # global vars
  search_code_l = innitVars[3]
  dimensions = innitVars[4]

  # generate the board
  flatten_list = generate_board(dimensions)
  button_list = generate_buttons(win, dimensions)
  
  # ask user to hide the pins and add them to board
  pin_location = hide_pins(win, search_code_l, button_list)
  print(pin_location)

  print("Stop!")
  win.getMouse()
  
  flatten_list = add_pins_to_board(flatten_list, pin_location)

  print("Computer will now search for the hidden pins!")

  flat_list = linear_search(flatten_list)
  found_pins = identify_flat_pins(flat_list, dimensions)
  print("Pins found!")
  print(found_pins)
