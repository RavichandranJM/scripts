#! /usr/bin/python

import random
num = random.randint(1, 100)
count = 0
while True:
    guess = int(raw_input("Guess the number:"))
    count += 1
    if guess == num:
        print("You took {0} guesses to find the number".format(count))
        break
    elif guess < num:
        print("you entered low")
    else:
        print("you entered high")
    cont = raw_input("Want to continue press y:")
    if cont in "Yy":
        continue
    else:
        break




