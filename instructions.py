
#*************************************************************************************/
# NAME: Alejandro Gutierrez Acosta, Lourdes Mariana Reyes Alegria, Sana Ala Y. Barakat
# ORGN: BS Computer Science & Artificial Intelligence / Algorithms & Data Structures
# PROJ: Mastermind+
# FILE: instructions.py
# DATE: Nov 27th 2022
#*************************************************************************************/

from graphics import *
from button import *

def instructions(win, num):
  # Runtime complexity:
  #   Worst-case    : O(1)
  #   Average-case  : O(1)
  # Main function to display the instruction screen for each of
  #   the games depending on input 'num'

  # Set image background : 400x566
    # 200, 283 is half the width and height, respectively, of the image/window
  if num == 0: #instructions for code breaker mode
    intro_img = Image(Point(200, 283),"pictures/inst_baker.gif")
    intro_img.draw(win)
  elif num == 1: #instructions for searching master mode
    intro_img = Image(Point(200, 283),"pictures/inst_search.gif")
    intro_img.draw(win)
  elif num == 2: #instructions for sorting master mode
    intro_img = Image(Point(200, 283),"pictures/inst_sorting.gif")
    intro_img.draw(win)
  
  done_button = Button(win, Point(200, 490), 250, 50, 'DONE')
  done_button.activate()
  
  done_button.rect.setFill(color_rgb(173,129,93))
  
  pt = win.getMouse()
  
  # Return to the main funciton that the user is done viewing the 
  if done_button.clicked(pt):
    next = 0

  return next