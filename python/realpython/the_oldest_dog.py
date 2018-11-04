#! /usr/bin/env python

class Dog(object):
    def __init__(this, age):
        this.age = age

d1 = Dog(5)
d2 = Dog(15)
d3 = Dog(25)

def get_biggest_number(*args):
    return max(args)

print "The oldest dog is {0} years old".format(get_biggest_number(d1.age, d2.age, d3.age))
