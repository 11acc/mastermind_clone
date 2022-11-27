from graphics import *
from button import *

import random as rand

def generate_buttons(win, dimensions):
  row, col = int(dimensions[0]), int(dimensions[-1])
  y = 210
  w, h = 48, 50
  buttons = []
  
  for r_sqr in range(row):
    x = 70
    for c_sqr in range(col):
      temp = [(6*r_sqr)+c_sqr, Button(win, Point(x, y), w, h, '')]
      temp[1].activate()
      buttons.append(temp)
      x += w+5
    y += h+5
    
  return buttons

def generate_board(dimensions):
  # Runtime complexity:
  # Worst case: O(n)
  # Avg. case: O(n)
  # Best case: O(n)

  row, col = int(dimensions[0]), int(dimensions[-1])
  print(f"Dimensions of board are {row}x{col}")

  flatten_list = [[i, 0] for i in range(row * col)]
  #search_board = [[([r,c], 0) for c in range(col)] for r in range(row)]

  return flatten_list


def unflatten(arr, dimensions):
  # Runtime complexity:
  # Worst case: O(n)
  # Avg. case: O(n)
  # Best case: O(n)

  row, col = int(dimensions[0]), int(dimensions[-1])
  newArr = [[(0, 0) for _ in range(row)] for _ in range(col)]
  for r in range(row):
    for c in range(col):
      pos = (6 * r) + c
      newArr[r][c] = arr[pos]
  return newArr


def hide_pins(win, search_code_l, button_list):
  # Runtime complexity:
  # Worst case: O(n)
  # Avg. case: O(n)
  # Best case: O(n)

  pin_location = []
  print("Input the locations where you will hide the pins")
  print(button_list)
  while len(pin_location) < search_code_l:
    pt = win.getMouse()

    for b in range(len(button_list)):
      if button_list[b][1].clicked(pt):
        loc = button_list[b][0]
        pin_location.append(loc)
        break

  return pin_location


def add_pins_to_board(flatten_list, pin_location):
  # Runtime complexity:
  # Worst case: O(n)
  # Avg. case: O(n)
  # Best case: O(n)

  for i in range(len(pin_location)):
    r, c = pin_location[i]
    pos = (6 * r) + c
    flatten_list[pos][1] = 1
  return flatten_list


def identify_flat_pins(pins, dimensions):
  # Identify which location in the 2d array are the found
  # pins from the 1d version of the array
  found_pins = []
  row_l = int(dimensions[0])

  for pin in pins:
    row, col = -1, -1
    counter = 0
    temp = pin

    if temp < 6:
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
  # Deliberate linear search when the user asks for easy mode
  # Runtime complexity:
  # Worst case: O(n)
  # Avg. case: O(n)
  # Best case: O(1)

  identified_pins = []
  for tile in flat_search_board:
    if tile[1] == 1:
      identified_pins.append(tile[0])

  return identified_pins
