#! /usr/bin/python

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __del__(self):
        name = self.__class__.__name__
        print "{} destroyed".format(name)
p1 = Point(10, 5)
p2 = p1
print id(p1), id(p2)
del p1
del p2
print id(p1), id(p2)

