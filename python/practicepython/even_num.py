#! /usr/bin/python
def even_num(l):
    return [ el for el in l if el % 2 == 0 ]
print even_num([1, 2, 3])
