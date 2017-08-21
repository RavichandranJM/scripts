#! /usr/bin/python

from multiprocessing import Process

def say_hello(name="world"):
    print("Hello {0}".format(name))
p = Process(target = say_hello, args = ("Ravi",))
p.start()
p.join()

