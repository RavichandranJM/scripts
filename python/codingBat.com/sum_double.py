#! /usr/bin/python

def sum_double(x, y):
    sum = x + y;
    if x == y:
        sum = sum * 2;
    return sum;

print sum_double(1, 2);
print sum_double(3, 2);
print sum_double(2, 2);


