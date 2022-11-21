
from graphics import *
from button import *

from code_maker import code_maker
from code_breaker import generate_guess

def maker(win, innitVars):
    print("mmmmmmmmmmmmmm")
    code_l = innitVars[1]
    
    #Seeting the pins
    win = GraphWin("maker", 270, 100)

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

    code = generate_guess(win, code_l, buttons)