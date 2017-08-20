# A random number guessing game for the number of 1 to 10, where the player guesses
#   the answer.

import random

secret_num = random.randint(1, 10)

while True:
    guess = int(input("Guess a number between 1 and 10: "))

    if guess == secret_num:
        print("You got it!. Your number was {}!".format(secret_num))
        break
    else:
        print("That's not it!")
