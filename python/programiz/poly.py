#! /usr/bin/env python

class Bird(object):
    def fly(self):
        return "can fly"
    def swim(self):
        return "can't swim"

class Penguin(object):
    def fly(self):
        return "can't fly"
    def swim(self):
        return "can swim"
def flyingTest(bird):
    return bird.fly()

blu = Bird()
peggy = Penguin()

blu.flyingTest()
peggy.flyingTest()

