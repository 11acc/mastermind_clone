
from graphics import *
from button import *

def instructions(win, num):
  no_name = False

  # set image background : 400x566
    # 200, 283 is half the width and height, respectively, of the image/window
  if num == 0:
    intro_img = Image(Point(200, 283),"pictures/code_maker_inst.gif")
    intro_img.draw(win)
  elif num == 1:
    intro_img = Image(Point(200, 283),"pictures/code_breaker_inst.gif")
    intro_img.draw(win)

  # done
  mode_w, mode_h = 250, 50
  mode_color = color_rgb(173,129,93)

  done_button = Button(win, Point(200, 490), mode_w, mode_h, 'DONE')
  done_button.activate()
  
  done_button.rect.setFill(mode_color)
  
  # click the mouse to signal done entering text
  win.getMouse()

  pt = win.getMouse()
  
  if done_button.clicked(pt):
    next = 0

  return next