#! /usr/bin/python

from multiprocessing import Lock

l = Lock()
l.acquire()
print "It is locked.. going to unlock"
l.release()
