#! /usr/bin/python

class DisplayData(object):
    def __init__(self):
        self.heading = "";
        self.value = 0;
def func1():
    obj1 = DisplayData();
    val = 2;
    heading =3;
    obj1 = func2(obj1, val, heading);
    print obj1.heading, obj1.value;

def func2(o, v, h):
    o.heading = h;
    o.value = v;
    return o
    #print o.value;
    
if __name__ == "__main__":
    func1()
