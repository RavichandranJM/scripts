#! /usr/bin/python
def primes_eratosthenes(limit):
    """Return all the prime numbers below or equal to the limit using the Sieve of Eratosthenes."""
    Limit = limit + 1
    numbers = []
    primelist = []
    for i in range(2, Limit):
        numbers.append(i)
    while True:
        if len(numbers) == 0:
            break
        prime = numbers[0]
        primelist.append(prime)
        for n in numbers:
            if n%prime == 0:
                numbers.remove(n)
    return primelist
 
def primes(limit):
    """Returns all the primes below using my algorithm"""
    Limit = limit+1
    primelist = []
    for i in range(2,Limit):
        prime = True
        for j in primelist:
            if i%j==0:
                prime = False
                break
        if prime == True:
            primelist.append(i)
    return primelist
 
def factor_withlist(n,primeslist):
    """Finds all the prime factors of the number n given a list that contains at least all the primes less than n."""
    factorlist = []
    for a in primeslist:
        if a > n:
            break
        b=True
        while  b==True:
            c = n%a
            if c==0:
                n=n/a
                factorlist.append(a)
            else:
                b=False
    return factorlist
 
def factor(n):
    """Finds all prime factors of n when a list of primes is not given."""
    primelist = primes(n)
    factorlist = []
    for a in primelist:
        if a > n:
            break
        b=True
        while  b==True:
            c = n%a
            if c==0:
                n=n/a
                factorlist.append(a)
            else:
                b=False
    return factorlist
