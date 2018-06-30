#! /usr/bin/python

class Computer(object):
    def __init__(self):
        self.__maxprice = 900
    def sell(self):
        return "selling price: {0}".format(self.__maxprice)
    def setMaxPrice(self, price):
        self.__maxprice = price
comp1 = Computer()
print comp1.sell()
comp1.__maxprice = 1200
print comp1.sell()
comp1.setMaxPrice(1200)
print comp1.sell()

