#! /usr/bin/python

num = int(raw_input("Enter a number:"))
for el in range(1, (num/2)+1):
    if num % el == 0:
        print(el)
