
from graphics import *

def breaker():
  #Setting the pins
  win = GraphWin("choose color", 270, 100)
  bluepin = Circle(Point(30,50), 10)
  bluepin.setFill("blue")
  
  redpin = Circle(Point(70,50), 10)
  redpin.setFill("red")

  orangepin = Circle(Point(110,50), 10)
  orangepin.setFill("orange")

  greenpin = Circle(Point(150,50), 10)
  greenpin.setFill("green")

  yellowpin = Circle(Point(190,50), 10)
  yellowpin.setFill("yellow")

  purplepin = Circle(Point(230,50), 10)
  purplepin.setFill("purple")

  #print the pins
  redpin.draw(win)
  bluepin.draw(win)
  greenpin.draw(win)
  yellowpin.draw(win)
  orangepin.draw(win)
  purplepin.draw(win)

  
  win.getMouse() # Pause to view result
  win.close()    # Close window when done