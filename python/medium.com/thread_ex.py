#!/usr/bin/env python

import threading

def square(d):
    print("square: ", d * d)
def quad(d):
    print("quad: ", d * d * d * d)
if __name__ == "__main__":
    num = 7
t1 = threading.Thread(target=square, args=(num,))
t2 = threading.Thread(target=quad, args=(num,))

t1.start()
t2.start()

#t1.join()
#t2.join()
