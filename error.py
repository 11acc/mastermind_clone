
#from termcolor import colored

def error(file, line, reason):
  x = " "
  #print(colored("Error: ", "red") + "File " + file + ".py, line " + line)
  print("Error: File " + file + ".py, line " + line)
  print(x*7 + "'" + reason + "'")
  