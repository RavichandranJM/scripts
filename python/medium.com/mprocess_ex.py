#!/usr/bin/env python

import multiprocessing

def square(d):
    print("square: ", d * d)
    result = d * d
    print(result)
def quad(d):
    print("quad: ", d * d * d * d)
if __name__ == "__main__":
    num = 7
    result = None
t1 = multiprocessing.Process(target=square, args=(num,))
t2 = multiprocessing.Process(target=quad, args=(num,))

t1.start()
t2.start()

t1.join()
t2.join()

print(result)

