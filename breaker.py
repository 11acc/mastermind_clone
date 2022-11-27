
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
  #colours = innitVars[2]
  #colours_n = innitVars[3]

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