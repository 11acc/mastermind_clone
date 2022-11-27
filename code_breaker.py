
from graphics import *
import random as rand


def code_breaker(innitVars):
    code_l = innitVars[1]
    colours = innitVars[2]
    colours_n = innitVars[3]

    print("Colour Key: ")
    for i in range(len(colours)):
        print(colours[i] + " - " + str(i))
    '''
    Colour Key: 
    red - 0
    blue - 1
    green - 2
    yellow - 3
    orange - 4
    purple - 5
    '''

    code = generate_code(colours_n, code_l)
    return code

### --- · --- ###

def generate_code(colour_list, code_l):
    code = []
    k = 0
    while k < code_l:
        choice = rand.choice(colour_list)
        if choice not in code:
            code.append(choice)
            k += 1
    return code

def generate_guess(win, code_l, buttons):
    guess_arr = []
    red = buttons[0]
    blue = buttons[1]
    green = buttons[2]
    yellow = buttons[3]
    orange = buttons[4]
    purple = buttons[5]

    while len(guess_arr) < code_l:
        pt = win.getMouse()
        if red.clicked(pt):
            print("red pin selected")
            guess_arr.append(0)
        elif blue.clicked(pt):
            print("blue pin selected")
            guess_arr.append(1)
        elif green.clicked(pt):
            print("green pin selected")
            guess_arr.append(2)
        elif yellow.clicked(pt):
            print("yellow pin selected")
            guess_arr.append(3)
        elif orange.clicked(pt):
            print("orange pin selected")
            guess_arr.append(4)
        elif purple.clicked(pt):
            print("purple pin selected")
            guess_arr.append(5)
    
    print(guess_arr)
    return guess_arr

def check_guess(code, guess):
    # rules:
    # if colour + position = black peg  ●
    # if colour + !position = white peg  ○
    # if !colour + !position = nothing ⏻
    # make them random
    perfect_guess = 0
    feedback_pegs = []

    for c in range(len(code)):
        for g in range(len(guess)):
            if guess[g] == code[c]:
                if g == c:
                    feedback_pegs.append(" ● ")
                    perfect_guess += 1
                    break
                else:
                    feedback_pegs.append(" ○ ")
                    break
    
    for _ in range(len(code)-len(feedback_pegs)):
        feedback_pegs.append(" ⏻ ")

    rand.shuffle(feedback_pegs)
    print(feedback_pegs)

    if perfect_guess == len(code):
        return True
    return False


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
