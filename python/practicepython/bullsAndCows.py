#! /usr/bin/python
import random

num = int("".join(random.sample('0123456789', 4)))
count = 0;
while True:
    count += 1;cows = 0;bulls = 0
    guess = int(raw_input("Guess the number:"))
    for index in range(len(str(guess))):
        if str(guess)[index] == str(num)[index]:
            bulls += 1
        elif str(guess)[index] in str(num):
            cows += 1
    print("{0} bulls {1} cows".format(bulls, cows))
    if guess == num:
        print("You guessed the number in {0} tries".format(count))
        break


