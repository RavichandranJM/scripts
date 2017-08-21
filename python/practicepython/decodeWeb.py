#! /usr/bin/python

import requests
from bs4 import BeautifulSoup as bs

url = "http://www.nytimes.com"
soup = bs(requests.get(url).text)
for item in soup.find_all(class_= "story-heading"):
    if item.a:
        print item.a.text.replace("\n", "").strip()
    else:
        print item.contents[0].strip()
