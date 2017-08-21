#! /usr/bin/python

num = int(raw_input("Enter a number:"))
if num % 2 == 0:
    print("Entered number is even")
else:
    print("Entered number is odd")
if num % 4 == 0:
    print("Given number is divisible by 4")
divider = int(raw_input("Enter another number:"))
if num % divider == 0:
    print("{0} divides {1} evenly".format(divider, num))
