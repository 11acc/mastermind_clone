
from graphics import *
from error import error
from innit_vars import innit_vars

from intro import intro
from instructions import instructions
from maker import maker
from breaker import breaker

###--- ··· ---###

def clear(win):
  for item in win.items[:]:
    item.undraw()
  win.update()


def main():
  # initialize variables
  # innitVars = [attempts, code_l, colours, colours_n]
  innitVars = innit_vars()

  win = GraphWin("GameIntro", 400, 566)
  main_intro(win, innitVars)
  win.close()


def main_intro(win, innitVars):
  # this variable will indicate the program if user selected
  # code maker or breaker, 0 and 1 repectively
  name = ""
  intro_output = -1
  
  intro_output, name = intro(win)

  if intro_output == 0:
    # code maker
    print("game mode: code maker")    
    clear(win)
    inst = instructions(win, intro_output)
    if inst == 0:
      clear(win)
    
    maker(win, innitVars)
  elif intro_output == 1:
    #code breaker
    print("game mode: code breaker")
    clear(win)
    inst = instructions(win, intro_output)
    if inst == 0:
      clear(win)

    breaker(win, innitVars)
  else:
    # catch error
    error("intro", "22", "output differs from 0 and 1")

###--- ··· ---###

main()