#!/usr/bin/env python
from collections import Counter

primeNumFile = "primenumbers.txt"
happyNumFile = "happynumbers.txt"

primeNums = []
happyNums = []
allNums = []

def readFile(fname):
    nums = []
    with open(fname) as f:
        rows = f.readlines()
        for row in rows:
            nums.append(int(row.strip()))
    return nums

primeNums = readFile(primeNumFile)
happyNums = readFile(happyNumFile)
allNums = primeNums + happyNums

counts = Counter(allNums)

print "Overlapping numbers:"
for key in counts:
    if counts[key] == 2:
        print key

