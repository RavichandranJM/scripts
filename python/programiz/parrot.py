#! /usr/bin/env python

class Parrot(object):
    species = "bird"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sing(self, song):
        return "{0} sings {1}".format(self.name, song)
    def dance(self):
        return "{0} is dancing".format(self.name)

bird1 = Parrot("bird1", 10)
bird2 = Parrot("bird2", 15)
print "{0} is a {1}".format(bird1.name, bird1.__class__.species)
print "{0} is a {1}".format(bird2.name, bird2.__class__.species)

print "{0} is {1} years old".format(bird1.name, bird1.age)
print "{0} is {1} years old".format(bird2.name, bird2.age)
print bird1.sing("happy")
print bird2.dance()

