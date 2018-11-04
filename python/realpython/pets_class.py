#!/usr/bin/env python
# Parent class
class Dog:

    # Class attribute
    species = 'mammal'

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_hungry = True

    # instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)

    def eat(self):
        self.is_hungry = False

    def walk(self):
        return "{} is walking!".format(self.name)

# Child class (inherits from Dog class)
class RussellTerrier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

# Child class (inherits from Dog class)
class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

class Pets(object):
        def __init__(self, dogs):
                self.dogs = dogs
        def mypets(self):
                any_pet_hungry = False
                print "I have {0} dogs".format(len(self.dogs))
                for dog in self.dogs:
                        print "{0} is {1}".format(dog.name, dog.age)
                        if dog.is_hungry:
                            any_pet_hungry = True
                print "And they're all {0}, of course".format(dog.species)
                if any_pet_hungry:
                        print "My dogs are hungry"
                else:
                        print "My dogs are not hungry"
                
        def feed(self):
                for dog in self.dogs:
                    dog.is_hungry = False

        def walk(self):
                for dog in self.dogs:
                    print dog.walk()

pets = Pets([Dog("Tom", 6), Dog("Fletcher", 7), Dog("Larry", 9)])
pets.feed()
pets.mypets()
pets.walk()
