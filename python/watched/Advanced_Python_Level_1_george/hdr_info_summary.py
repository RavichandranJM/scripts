#!/usr/bin/env python

import httplib

conn = httplib.HTTPConnection("www.google.com")
conn.request("HEAD", "/index.html")
res = conn.getresponse()
print res.getheaders()

