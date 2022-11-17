
import random as rand

def guess_pins():
    attempts = 6
    code_l = 4

    colours = ["red", "blue", "green", "yellow", "orange", "purple"]
    colours_n = [0,1,2,3,4,5]

    print("Colour Key: ")
    for i in range(len(colours)):
        print(colours[i] + " - " + str(i))

    code = generate_code(colours_n, code_l)
    print(code)

    win_condition = None
    for j in range(attempts):
        guess = generate_guess()
        win_condition = check_guess(code, guess)
        if win_condition:
            print("Congratulations you won in " + str(j+1) + " attempts!")
            break
    
    if win_condition == False:
        print("Sorry you ran out of attempts! Better luck next time.")

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

def generate_guess():
    guess_arr = []

    print("Input guesses separated by spaces: ")
    input_var = input().split()

    for item in range(len(input_var)):
        guess_arr.append(int(input_var[item]))

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

### --- · --- ###

guess_pins()