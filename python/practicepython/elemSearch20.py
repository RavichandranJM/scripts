#!/usr/bin/env python

def searchElem(nums, num):
    left = 0
    right = len(nums)
#    if nums[-1] < num:
#        return False
#    elif nums[0] > num:
#        return False
    items = nums
    while len(items) != 1:
        items = items[left:right]
        middle = len(items) / 2
        #print items, middle, left, right
        if items[middle] < num:
            left = middle
            print "left assigned"
        elif items[middle] > num:
            right = middle
        else:
            return True
    if items[left] == num:
        return True
    else:
        return False

if searchElem([1, 2, 3, 4, 5, 6], 0):
    print "It is exist"
else:
    print "It is not exist"
    
