#! /usr/bin/python
#Here's some code that might accomplish this:

from random import choice
import sys
def generateRandomString(length):
    output = ""
    for i in range(length):
        #pick a random bracket
        output = output + choice(['[',']'])
    return output

#As far matching the actual brackets

def isCorrectParens(someCode):
    choices = ['[',']']
    stack = []
    for c in someCode:
        if c in choices:
            if c == ']':
                #pop off the stack
                if len(stack) == 0:
                    return False
                else:
                    stack.pop()
            else:
                #push onto the stack
                stack.append(c)
    if stack:
        return False
    return True

#Here is the code for how you would take input from the command line

if len(sys.argv) == 1:
    #test a random string
    generatedString = generateRandomString(10)
    print "Generated random string: " + generatedString
    print "Is valid parens :" + str(isCorrectParens(generatedString))

if len(sys.argv) == 2:
    #test the inputted string
    print "Inputted string: "+sys.argv[1]
    print "Valid parens? :"+str(isCorrectParens(sys.argv[1]))
