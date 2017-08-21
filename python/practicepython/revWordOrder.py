#! /usr/bin/python

s = raw_input("Enter a string with multiple words:")
for el in s.split()[::-1]:
    print el,

