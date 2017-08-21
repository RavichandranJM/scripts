#! /usr/bin/python

num = int(raw_input("Enter a number:"))
print([el for el in [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] if el < num])
