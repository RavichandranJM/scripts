#! /usr/bin/python

class Bird(object):
    def __init__(self):
        print 'Bird is ready'
    def whoIsThis(self):
        return "Bird"
    def swim(self):
        return "swim faster"

class Penguin(Bird):
    def __init__(self):
        super(Penguin, self).__init__()
        print "Penguin is ready"
    def whoIsThis(self):
        return "Penguin"
    def run(self):
        return "Run faster"

peggy = Penguin()
print peggy.whoIsThis()
print peggy.swim()
print peggy.run()
