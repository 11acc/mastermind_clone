
from graphics import *
from error import error
from intro import intro
from breaker import breaker
from guess_pins import guess_pins

###--- ··· ---###

def main():
  win = GraphWin("GameIntro", 400, 566)
  main_intro(win)

def main_intro(win):
  # this variable will indicate the program if user selected
  # code maker or breaker, 0 and 1 repectively
  name = ""
  intro_output = -1
  
  intro_output, name = intro(win)

  if intro_output == 0:
    # code maker
    print("game mode: code maker")    
  elif intro_output == 1:
    #code breaker
    print("game mode: code breaker")
    #breaker()
    guess_pins()
  else:
    # catch error
    error("intro", "22", "output differs from 0 and 1")

###--- ··· ---###

main()