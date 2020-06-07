#!/usr/local/bin/python3.7
from collections import deque
import itertools
def moving_average(iterable, n=3):
    # moving_average([40, 30, 50, 46, 39, 44]) --> 40.0 42.0 45.0 43.0
    # http://en.wikipedia.org/wiki/Moving_average
    it = iter(iterable)
    d = deque(itertools.islice(it, n-1))
    d.appendleft(0)
    print(d)
    s = sum(d)
    for elem in it:
        print(elem)
        s += elem - d.popleft()
        d.append(elem)
        yield s / n

res = moving_average([40, 30, 50, 46, 39, 44])
for item in res:
    print(item)