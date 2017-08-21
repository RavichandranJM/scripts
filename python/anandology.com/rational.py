#! /usr/bin/python

class Rational(object):
    def __init__(self, n, d = 1):
        self.n = n
        self.d = d
    def __add__(self, other):
        return Rational(self.n * other.d + self.d * other.n, self.d * other.d)
    def __sub__(self, other):
        return Rational(self.n * other.d - self.d * other.n, self.d * other.d)
    def __mul__(self, other):
        return Rational(self.n * other.n, self.d * other.d)
    def __div__(self, other):
        return Rational(self.n * other.d, self.d * other.n)
    def __str__(self):
        return "{0}/{1}".format(self.n, self.d)
a = Rational(5,7)
b = Rational(3,7)
print a + b
print a - b
print a * b
print a / b
