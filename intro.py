
#*************************************************************************************/
# NAME: Alejandro Gutierrez Acosta, Lourdes Mariana Reyes Alegria, Sana Ala Y. Barakat
# ORGN: BS Computer Science & Artificial Intelligence / Algorithms & Data Structures
# PROJ: Mastermind+
# FILE: intro.py
# DATE: Nov 27th 2022
#*************************************************************************************/

from graphics import *
from button import *

def intro(win):
  # Runtime complexity:
  #   Worst-case    : O(1)
  #   Average-case  : O(1)
  # Main function to display the necessary visuals in the main menu

  # Set image background : 400x566
    # 200, 283 is half the width and height, respectively, of the image/window
  intro_img = Image(Point(200, 283),"pictures/MASTERMIND.gif")
  intro_img.draw(win)

  # get name from box
  inputText = Entry(Point(200, 190), 31)  # 5 is the space we are going to reserve to put the text
  inputText.setFill(color_rgb(173,129,93))
  inputText.setText("")
  inputText.draw(win)

  # Submit box
  button = Text(Point(200, 240), "Submit")
  button.draw(win)
  # 200, 283
  Rectangle(Point(155, 230), Point(240, 250)).draw(win)

  # choose maker/breaker
  mode_w, mode_h = 250, 50
  mode_color = color_rgb(173,129,93)
  
  breaker_button = Button(win, Point(200, 365), mode_w, mode_h, 'CODE BREAKER')
  breaker_button.activate()
  
  search_button = Button(win, Point(200, 450), mode_w, mode_h, 'SEARCH MASTER')
  search_button.activate()
  
  sort_button = Button(win, Point(200, 535), mode_w, mode_h, 'SORT MASTER')
  sort_button.activate()
  
  breaker_button.rect.setFill(mode_color)
  search_button.rect.setFill(mode_color)
  sort_button.rect.setFill(mode_color)
  
  # Click the mouse to signal done entering text
  win.getMouse()
  
  name = inputText.getText()
  print(name)

  pt = win.getMouse()
  
  if breaker_button.clicked(pt):
    gamemode = 0
  elif search_button.clicked(pt):
    gamemode = 1
  elif sort_button.clicked(pt):
    gamemode = 2

  return gamemode, name