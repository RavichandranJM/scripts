#!/usr/bin/env python

inFile = "nameslist.txt"
namesCount = {}

with open(inFile) as inFileObj:
    rows =  inFileObj.readlines()
    for row in rows:
        row = row.strip()
        if namesCount.has_key(row):
            namesCount[row] += 1
        else:
            namesCount[row] = 1
for pair in namesCount.items():
    print pair
