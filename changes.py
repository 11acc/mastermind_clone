
from graphics import *
from button import *

from code_breaker import code_breaker
from code_breaker import generate_guess
from code_breaker import check_guess
from code_breaker import color_click_change
from code_breaker import clues_color


def breaker(win, innitVars):
  background = Image(Point(200, 283), "pictures/Breaker.gif")
  background.draw(win)

  attempts = innitVars[0]
  code_l = innitVars[1]
  colour = innitVars[2]
  colours_n = innitVars[3]

  # 1.1 create buttons
  red_btn = Button(win, Point(107, 482), 14, 14, '')
  blue_btn = Button(win, Point(144, 482), 14, 14, '')
  green_btn = Button(win, Point(182, 482), 14, 14, '')
  yellow_btn = Button(win, Point(219, 482), 14, 14, '')
  orange_btn = Button(win, Point(256, 482), 14, 14, '')
  purple_btn = Button(win, Point(293, 482), 14, 14, '')

  buttons = [red_btn, blue_btn, green_btn, yellow_btn, orange_btn, purple_btn]

  # 1.2 activate buttons
  red_btn.activate()
  blue_btn.activate()
  green_btn.activate()
  yellow_btn.activate()
  orange_btn.activate()
  purple_btn.activate()

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

  # Call function to generate code
  code = code_breaker(win, innitVars)
  print(code)

  win_condition = None
  #y-coordinate
  y_num = 27.7
  for i in range(attempts):
    guess = generate_guess(win, code_l, buttons)
    #To display the guessed code
    color_click_change(win, 92, y_num, 14.5, guess)
    
    # Check for win condition
    win_condition, cluesList = check_guess(code, guess)

    # To display clues
    clues_color(cluesList)
    
    if win_condition:
      color_click_change(win, 92, y_num, 14.5, guess)
      print("Congratulations you won in " + str(i + 1) + " attempts!")
      break
    y_num += 40

  if win_condition == False:
    color_click_change(win, 92, y_num, 14.5, guess)
    print("Sorry you ran out of attempts! Better luck next time.")

    

# -----------------------------------
'''
sorting - sort pins in a particular order
search - hide mastermind pins in a table #alex

# solo 1, o 2 si podemos, de estos:
trees - ?
hashtables - ?
heaps - ?
graphs - ?
'''

# -----------------------------------


#This function is to create the colors that change color depending on which button is clicked
def color_click_change(win, x_coor, y_coor, size, code):
  pins = []
  pin = Circle(Point(x_coor, y_coor), size)
  pin2 = Circle(Point(x_coor + 37, y_coor), size)
  pin3 = Circle(Point(x_coor + 74, y_coor), size)
  pin4 = Circle(Point(x_coor + 112, y_coor), size)
  pins.append(pin)
  pins.append(pin2)
  pins.append(pin3)
  pins.append(pin4)
  num = 0
  for i in pins:
    if code[num] == 0:
      i.setFill("red")
    elif code[num] == 1:
      i.setFill("blue")
    elif code[num] == 2:
      i.setFill("green")
    elif code[num] == 3:
      i.setFill("yellow")
    elif code[num] == 4:
      i.setFill("orange")
    elif code[num] == 5:
      i.setFill("purple")
    num += 1
    i.draw(win)

def clues_color(cluesList):
  pass
