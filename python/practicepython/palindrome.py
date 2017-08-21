#! /usr/bin/python

def palindrome(s):
    if s == s[::-1]:
        print("{0} is a palindrome".format(s))
palindrome("name")
palindrome("madam")
