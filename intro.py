
from graphics import *
from button import *

def intro(win):
  print("Program runs.")
  no_name = False

  # set image background : 400x566
    # 200, 283 is half the width and height, respectively, of the image/window
  intro_img = Image(Point(200, 283),"pictures/MASTERMIND.gif")
  intro_img.draw(win)

  # get name from box
  inputText = Entry(Point(200, 190), 31)  # 5 is the space we are going to reserve to put the text
  inputText.setFill(color_rgb(173,129,93))
  inputText.setText("")
  inputText.draw(win)

  #Submit box
  button = Text(Point(200, 240), "Submit")
  button.draw(win)
  # 200, 283
  Rectangle(Point(155, 230), Point(240, 250)).draw(win)

  # choose maker/breaker
  mode_w, mode_h = 250, 50
  mode_color = color_rgb(173,129,93)
  
  maker_button = Button(win, Point(200, 365), mode_w, mode_h, 'CODE MAKER')
  maker_button.activate()
  
  breaker_button = Button(win, Point(200, 450), mode_w, mode_h, 'CODE BREAKER')
  breaker_button.activate()
  
  maker_button.rect.setFill(mode_color)
  breaker_button.rect.setFill(mode_color)
  
  # click the mouse to signal done entering text
  win.getMouse()
  
  name = inputText.getText()
  print(name)
  if name == "" or name == " ":
    no_name = True
  
  if no_name == True:
    name = "Jullianne"


  pt = win.getMouse()
  
  if maker_button.clicked(pt):
    gamemode = 0
  elif breaker_button.clicked(pt):
    gamemode = 1

  # code breaker / maker
  #gamemode = -1
  
  # add instructions
    # TODO

  # return maker/breaker, and name
  return gamemode, name