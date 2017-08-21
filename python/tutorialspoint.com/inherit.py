#! /usr/bin/python

class Parent(object):
    pAttr = 100
    def __init__(self):
        print "Calling Parent __init__"
    def pMethod(self):
        print "Calling Parent Method"
    def setAttr(self, attr):
        Parent.pAttr = attr
    def getAttr(self):
        return Parent.pAttr
class Child(Parent):
    def __init__(self):
        print "Calling child __init__"
    def cMethod(self):
        print "Calling child method"
c = Child()
c.cMethod()
c.pMethod()
c.setAttr(50)
print c.getAttr()

