
#*************************************************************************************/
# NAME: Alejandro Gutierrez Acosta, Lourdes Mariana Reyes Alegria, Sana Ala Y. Barakat
# ORGN: BS Computer Science & Artificial Intelligence / Algorithms & Data Structures
# PROJ: Mastermind+
# FILE: sorting.py
# DATE: Nov 27th 2022
#*************************************************************************************/

from graphics import *
from queue_stack import *
from button import *
import random
import time

from code_breaker import generate_guess

def clear(win):
  # Runtime complexity:
  #   Worst-case    : O(n)
  #   Average-case  : O(n)
  # Clear for multiple items
  for item in win.items[:]:
    item.undraw()
  win.update()
  
def sorting_master(win, innitVars):
  # Runtime complexity:
  #   Worst-case    : O(1)
  #   Average-case  : O(1)
  # Main function to manage the visuals and the necessary funcitons
  #  for sorting to work
  background = Image(Point(200, 283),"pictures/code_sorter.gif")
  background.draw(win)
    
  code_l = innitVars[1]
  colours_map = innitVars[2]

  # 1.1 create buttons
  red_btn = Button(win, Point(107, 300), 14, 14, '')
  blue_btn = Button(win, Point(144, 300), 14, 14, '')
  green_btn = Button(win, Point(182, 300), 14, 14, '')
  yellow_btn = Button(win, Point(219, 300), 14, 14, '')
  orange_btn = Button(win, Point(256, 300), 14, 14, '')
  purple_btn = Button(win, Point(293, 300), 14, 14, '')
  undo_btn = Button(win, Point(200, 530), 50, 16, 'Undo')
  scramble_btn = Button(win, Point(200, 480), 100, 16, 'Scramble')

  buttons = [red_btn, blue_btn, green_btn, yellow_btn, orange_btn, purple_btn, undo_btn]

  # 1.2 activate buttons
  red_btn.activate()
  blue_btn.activate()
  green_btn.activate()
  yellow_btn.activate()
  orange_btn.activate()
  purple_btn.activate()
  undo_btn.activate()
  scramble_btn.activate()

  # 2.1 create pins
  redpin = Circle(Point(107, 300), 14)
  bluepin = Circle(Point(143, 300), 14)
  greenpin = Circle(Point(181, 300), 14)
  yellowpin = Circle(Point(218, 300), 14)
  orangepin = Circle(Point(256, 300), 14)
  purplepin = Circle(Point(293, 300), 14)

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

  # y-coordinate
  y_cord = 200
  guess = generate_guess(win, 9, y_cord, buttons, colours_map)

  # Create hashmap to save code generated and mess it up
  colors_mess = {}
  num = 8
  for i in range(9):
    col = guess.pop()
    colors_mess[num] = (col)
    num -= 1

  print(colors_mess)

  pt = win.getMouse()
  if scramble_btn.clicked(pt):
    clear(win)
    # Put new image
    background2 = Image(Point(200, 283),"pictures/scrambled.gif")
    background2.draw(win)
    # Create buttons for merge sort and quicksort
    quick_btn = Button(win, Point(200, 450), 100, 20, 'Quicksort')
    merge_btn = Button(win, Point(200, 480), 100, 20, 'Mergesort')

    quick_btn.activate()
    merge_btn.activate()

    # Mess up the organization of the pins
    randomls = []
    while len(randomls) < 9:
      num = random.randrange(9)
      if num not in randomls:
        randomls.append(num)
    
    print(randomls)
    color_click_change2(win, 50, 210, 14, randomls, colors_mess)
    
    pt = win.getMouse()

    if quick_btn.clicked(pt):
      clear(win)
      quick_bg = Image(Point(200, 283),"pictures/sorted!.gif")
      quick_bg.draw(win)
      # Quick Sort 
      start_time = time.time()
      srt = quicksort(randomls)
      print("Quicksort took --- %s seconds ---" % (time.time() - start_time))
      color_click_change2(win, 53, 260, 14, srt, colors_mess)
      txt = Text(Point(200, 360), "--- %s seconds ---" % (time.time() - start_time))
      txt.draw(win)
      pt = win.getMouse()
      
    elif merge_btn.clicked(pt):
      clear(win)
      merge_bg = Image(Point(200, 283),"pictures/sorted!.gif")
      merge_bg.draw(win)
      # Merge Sort
      start_time = time.time()
      srt = merge_sort(randomls)
      print("Merge Sort took --- %s seconds ---" % (time.time() - start_time))
      color_click_change2(win, 53, 260, 14, srt, colors_mess)
      txt = Text(Point(200, 360), "--- %s seconds ---" % (time.time() - start_time))
      txt.draw(win)
      pt = win.getMouse()

def generate_guess(win, code_l, y_cord, buttons, colours_map):
  # Runtime complexity:
  #   Worst-case    : O(n log n)
  #   Average-case  : O(n log n)
  # Generates guess for the sorting game
  guess_stack = Stack()
  red = buttons[0]
  blue = buttons[1]
  green = buttons[2]
  yellow = buttons[3]
  orange = buttons[4]
  purple = buttons[5]
  undo = buttons[6]
  undo_trig = None
  x_cord = 50
  size = 14.5

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
      if guess_stack.stack_size >= 1: 
        undo_trig = True  
        print("trying to undo!")
        guess_stack.pop()
        x_cord -= 37
        indiv_pin_undo(win, guess_stack, x_cord, y_cord, size)
    
    if button_clicked:
      indiv_pin_change(win, guess_stack, x_cord, y_cord, size)
      x_cord += 37
    
  return guess_stack


def indiv_pin_change(win, guess_stack, x_cord, y_coor, size):
  # Runtime complexity:
  #   Worst-case    : O(1)
  #   Average-case  : O(1)
  # Real time pin change
  pin = Circle(Point(x_cord, y_coor), size)
  pin.setFill(guess_stack.top.value)
  pin.draw(win)


def indiv_pin_undo(win, guess_stack, x_cord, y_coor, size):
  # Runtime complexity:
  #   Worst-case    : O(1)
  #   Average-case  : O(1)
  # Real time pin undo
  pin = Circle(Point(x_cord, y_coor), size)
  pin.setFill("white")
  pin.draw(win)

# A function to show the pins to the user after they have been scrambled
def color_click_change2(win, x_coor, y_coor, size, randomls, colors_mess):
  # Runtime complexity:
  #   Worst-case    : O(1)
  #   Average-case  : O(1)
  # Real time pin change when clicked
  pins = []
  pin = Circle(Point(x_coor, y_coor), size)
  pin2 = Circle(Point(x_coor + 35, y_coor), size)
  pin3 = Circle(Point(x_coor + 70, y_coor), size)
  pin4 = Circle(Point(x_coor + 105, y_coor), size)
  pin5 = Circle(Point(x_coor + 140, y_coor), size)
  pin6 = Circle(Point(x_coor + 175, y_coor), size)
  pin7 = Circle(Point(x_coor + 210, y_coor), size)
  pin8 = Circle(Point(x_coor + 245, y_coor), size)
  pin9 = Circle(Point(x_coor + 280, y_coor), size)
  pins.append(pin)
  pins.append(pin2)
  pins.append(pin3)
  pins.append(pin4)
  pins.append(pin5)
  pins.append(pin6)
  pins.append(pin7)
  pins.append(pin8)
  pins.append(pin9)
  num = 0
  for i in pins:
    if randomls[num] == 0:
      i.setFill(colors_mess[0])
    elif randomls[num] == 1:
      i.setFill(colors_mess[1])
    elif randomls[num] == 2:
      i.setFill(colors_mess[2])
    elif randomls[num] == 3:
      i.setFill(colors_mess[3])
    elif randomls[num] == 4:
      i.setFill(colors_mess[4])
    elif randomls[num] == 5:
      i.setFill(colors_mess[5])
    elif randomls[num] == 6:
      i.setFill(colors_mess[6])
    elif randomls[num] == 7:
      i.setFill(colors_mess[7])
    elif randomls[num] == 8:
      i.setFill(colors_mess[8])
    num += 1
    i.draw(win)


def quicksort(arr):
  # Runtime complexity:
  #   Worst-case    : O(n log n)
  #   Average-case  : O(n log n)
  if len(arr) < 2:
    return arr
  pivot = arr[0]
  left = [element for element in arr[1:] if element < pivot]
  right = [element for element in arr[1:] if element >= pivot]
  return quicksort(left) + [pivot] + quicksort(right)

def combine(left, right):
  # Runtime complexity:
  #   Worst-case    : O(n log n)
  #   Average-case  : O(n log n)
  # Function to aid merge sort
  result = [0] * (len(left) + len(right)) # Initialize a zero array of the size of both left and right combined. This array will contain all the values of left and right arrays, respecing the order
  l, r, k = 0, 0, 0
  while l < len(left) and r < len(right): # While we have elements to add to the result array, on both the left and right sub arrays
    if left[l] < right[r]:  # The element we are checking at left (that at position `l`) is smaller than tat at the right array (that at `r` position).
      result[k] = left[l]  # So we add it to the next available position at the `result` array
      l += 1 # Increase the `l` pointer, so at the next iteration of the while loop we use the next element of `left` in the comparison
    else:  # Otherwise, store the element at `right`
      result[k] = right[r]
      r +=1
    k += 1
  while l < len(left): # In case the 'right' array was completely traversed, add the remaining elements of 'left'
    result[k] = left[l]
    l += 1
    k += 1
  while r < len(right): # In calse the 'left' array was completely traversed during the first while loop, add the remaining elements of 'right'
    result[k] = right[r]
    r += 1
    k += 1
  return result
  
def merge_sort(randomls):
  # Runtime complexity:
  #   Worst-case    : O(n)
  #   Average-case  : O(n)
  if len(randomls) < 2: # Base case: an array of size 1 or 0 is considered to be already sorted
    return randomls
  mid = len(randomls) // 2
  # Split the given `arr` in two halves: `left` and `right`
  left = randomls[:mid]
  right = randomls[mid:]
  sorted_left = merge_sort(left)
  sorted_right = merge_sort(right)
  return combine(sorted_left, sorted_right)