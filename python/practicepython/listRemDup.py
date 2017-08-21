#! /usr/bin/python

import random

l = random.sample(range(1, 100), 10)
l = [1, 2, 3, 3, 2, 4]
print("Random list:{0}".format(l))
def removedupList(l):
    temp = []
    for el in l:
        if el not in temp:
            temp.append(el)
    return temp
def removedupSet(l):
    return list(set(l))
print("Remove duplicate elements using list: {0}".format(removedupList(l)))
print("Remove duplicate elements using set: {0}".format(removedupSet(l)))

