#! /usr/bin/python

class Count(object):
    __count = 0
    def inc(self):
        self.__count += 1
        print "count: ", self.__count
c = Count()
c.inc()
c.inc()
print c._Count__count
print c.__count
