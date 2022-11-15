
import random as rand

def main():
    colours = ["red", "blue", "green", "yellow", "orange", "purple"]
    colours_n = [0,1,2,3,4,5]

    print("Colour Key: ")
    for i in range(len(colours)):
        print(colours[i] + " - " + str(i))

    code = generate_code(colours_n)
    guess = generate_guess()
    check_guess(code, guess)
    
### --- · --- ###

def generate_code(colour_list):
    code = []
    j = 0
    while j < 4:
        choice = rand.choice(colour_list)
        if choice not in code:
            code.append(choice)
            j += 1
    return code

def generate_guess():
    print("Input guess (4 items separated by spaces): ")
    one, two, three, four = input().split()
    one, two, three, four = [int(x) for x in [one, two, three, four]]

    guess_arr = [one, two, three, four]
    return guess_arr

def check_guess(code, guess):
    for k in range(len(guess)):
        if code[k] != guess [k]:
            print("Position " + str(k) + "incorrect")

### --- · --- ###

main()