#!/usr/bin/env python

import string

v = {"var1": "r"}

x = string.Template("""
        Name var1     : ${var1}chandran
""")
print x.substitute(v)

y = """
    Name var : %(var1)chandran
    """
print "interpolation", y%v
