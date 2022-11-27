
#*************************************************************************************/
# NAME: Alejandro Gutierrez Acosta, Lourdes Mariana Reyes Alegria, Sana Ala Y. Barakat
# ORGN: BS Computer Science & Artificial Intelligence / Algorithms & Data Structures
# PROJ: Mastermind+
# FILE: clear.py
# DATE: Nov 27th 2022
#*************************************************************************************/

def clear(win):
  # Runtime complexity:
  #   Worst-case    : O(1)
  #   Average-case  : O(1)
  # clear()'s purpose is to remove whichever current graphic window 
  #   is shown as an output in order for other windows to be shown 
  #   to the user.
  for item in win.items[:]:
    item.undraw()
  win.update()