#! /usr/bin/python

def countLines(fname):
    with open(fname) as f:
        return len(f.readlines())

def countChar(fname):
    with open(fname) as f:
        return len(f.read())

def test(fname):
    print countLines(fname)
    print countChar(fname)

if __name__ == '__main__':
    test("mymod.py")

