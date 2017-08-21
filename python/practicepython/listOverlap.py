#! /usr/bin/python
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
common = []
for el in a:
    if el not in common:
        common.append(el)
for el in b:
    if el not in common:
        common.append(el)
print(common)
