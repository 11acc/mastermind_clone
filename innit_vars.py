
#*************************************************************************************/
# NAME: Alejandro Gutierrez Acosta, Lourdes Mariana Reyes Alegria, Sana Ala Y. Barakat
# ORGN: BS Computer Science & Artificial Intelligence / Algorithms & Data Structures
# PROJ: Mastermind+
# FILE: innit_vars.py
# DATE: Nov 27th 2022
#*************************************************************************************/

def innit_vars():
  # Runtime complexity:
  #   Worst-case    : O(1)
  #   Average-case  : O(1)
  # Global function for easy access to variables used many times
  #   accross many different files of the game
  attempts = 10
  code_l = 4
  colours_map = {0:"red", 1:"blue", 2:"green", 3:"yellow", 4:"orange", 5:"purple"}
  search_code_l = 4
  search_dimensions = "6x6"

  innitVars = [attempts, code_l, colours_map, search_code_l, search_dimensions]

  return innitVars