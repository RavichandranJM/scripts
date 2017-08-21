#! /usr/bin/python
def func(a):
    if a in ['a', 'e', 'i', 'o', 'u']:
        return True
    return False
def translate(s):
    ret = ""
    for char in s:
        if not func(char) and char != " ":
            ret = ret + char + 'o' + char
        else:
            ret = ret + char
    return ret
