#! /usr/bin/python

import random

def firstLast(l):
    return [l[0], l[-1]]
def randList():
    return random.sample(range(1, 100), 10)
l = randList()
print("Random list: {0}".format(l))
print("First and last elements: {0}".format(firstLast(l)))
