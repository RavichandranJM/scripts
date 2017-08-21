#! /usr/bin/python

num = int(raw_input("Enter a number:"))
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

for n in range(1, num+1):
    print(fib(n))

