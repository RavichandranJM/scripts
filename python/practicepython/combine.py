#! /usr/bin/python


import random

l1 = random.sample(range(1, 100), 15)
l2 = random.sample(range(1, 100), 16)

def combine(l1, l2):
    return [el for el in set(l1) if el in l2]
print("list1: {0}, list2: {1}".format(l1, l2))
print(combine(l1, l2))

