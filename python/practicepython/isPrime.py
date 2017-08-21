#! /usr/bin/python

def isPrime(n):
    for num in range(2, (n/2) + 1):
        if n % num == 0:
            return False
    return True

n = int(raw_input("Enter a number:"))
if isPrime(n):
    print("Given {0} is prime".format(n))
else:
    print("Given {0} is not prime".format(n))

