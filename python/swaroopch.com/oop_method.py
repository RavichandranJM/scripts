#! /usr/bin/python
class Person(object):
    def say_hi(self):
        print "Hai"
    @classmethod
    def say(cls):
        print "hello"
    @staticmethod
    def static():
        print "hello1"
p = Person()
p.say_hi()
Person().say_hi()
Person.say()
Person.static()
Person().static()
