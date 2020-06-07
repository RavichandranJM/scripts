#!/usr/bin/env python3

import sys

if __name__ == '__main__':
    isGuessed = False
    guessCount = 0
    start = 0
    end = 100
    while not isGuessed:
        guess = int((start + end) // 2)
        guessCount += 1
        print("\n{0} is the number".format(guess))
        print("Enter 'a' if your number is above than my guess")
        print("Enter 'b' if your number is below than my guess")
        print("Enter 'y' if my guess is correct")
        print("Enter 'q' to quit guessing game")
        resp = input("your input: ")
        if resp == "y":
            print("It took {1} guess to find the number".format(guess, guessCount))
            break
        elif resp == "a":
            start = guess + 1
        elif resp == "b":
            end = guess - 1
        elif resp == "q":
            sys.exit(0)
        else:
            print("Please enter only accepted input!!!!!.....")
            
            

