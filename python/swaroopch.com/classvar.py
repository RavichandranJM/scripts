#! /usr/bin/python

class Robot(object):
    pop = 0
    def __init__(self, name):
        self.name = name
        print "Initalizing {}".format(self.name)
        Robot.pop += 1
    def die(self):
        print "Removing {}".format(self.name)
        Robot.pop -= 1
        if Robot.pop == 0:
            print "{} is last one".format(self.name)
        else:
            print "we have {:d} left".format(Robot.pop)
    def say_hi(self):
        print "Greetings this is from {0}".format(self.name)
    @classmethod
    def howmany(cls):
        print "We have {:d} robots".format(cls.pop)
r1 = Robot("R1")
r1.say_hi()
Robot.howmany()
r1.__doc__
Robot.__doc__
Robot.say_hi.__doc__
r2 = Robot("R2")
r2.say_hi()
Robot.howmany()
r1.die()
r2.die()
Robot.howmany()

    
