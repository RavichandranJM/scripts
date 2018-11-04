#!/usr/bin/env python

import urllib, htmllib, formatter, sys

u = urllib.urlopen("https://teamtreehouse.com/")
dta = u.read()

fmt = formatter.AbstractFormatter(formatter.DumbWriter(sys.stdout))
pobj = htmllib.HTMLParser(fmt)
pobj.feed(dta)
pobj.close()
