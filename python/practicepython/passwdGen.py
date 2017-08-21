#! /usr/bin/python
import string
import random

weakpasswdList = string.ascii_letters
strongpasswdList = weakpasswdList + string.digits + string.punctuation
choice = raw_input("How you want password be:")
if choice == "weak":
    print("Password:{0}".format("".join(random.sample(weakpasswdList, 8))))
else:
    print("Password:{0}".format("".join(random.sample(strongpasswdList, 8))))
