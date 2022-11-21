
from graphics import *
from button import *

from code_breaker import code_breaker
from code_breaker import generate_guess
from code_breaker import check_guess


def breaker(win, innitVars):
  attempts = innitVars[0]
  code_l = innitVars[1]
  colours = innitVars[2]
  colours_n = innitVars[3]

  #Seeting the pins
  win = GraphWin("choose color", 270, 100)

  # 1.1 create buttons
  red_btn = Button(win, Point(30, 50), 10, 10, '')
  blue_btn = Button(win, Point(70, 50), 10, 10, '')
  green_btn = Button(win, Point(110, 50), 10, 10, '')
  yellow_btn = Button(win, Point(150, 50), 10, 10, '')
  orange_btn = Button(win, Point(190, 50), 10, 10, '')
  purple_btn = Button(win, Point(230, 50), 10, 10, '')

  buttons = [red_btn, blue_btn, green_btn, yellow_btn, orange_btn, purple_btn]

  # 1.2 activate buttons
  red_btn.activate()
  blue_btn.activate()
  green_btn.activate()
  yellow_btn.activate()
  orange_btn.activate()
  purple_btn.activate()

  # 2.1 create pins
  redpin = Circle(Point(30, 50), 10)
  bluepin = Circle(Point(70, 50), 10)
  greenpin = Circle(Point(110, 50), 10)
  yellowpin = Circle(Point(150, 50), 10)
  orangepin = Circle(Point(190, 50), 10)
  purplepin = Circle(Point(230, 50), 10)

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
  code = code_breaker(innitVars)
  print(code)

  win_condition = None
  for i in range(attempts):
    guess = generate_guess(win, code_l, buttons)
    win_condition = check_guess(code, guess)
    if win_condition:
      print("Congratulations you won in " + str(i + 1) + " attempts!")
      break

  if win_condition == False:
    print("Sorry you ran out of attempts! Better luck next time.")