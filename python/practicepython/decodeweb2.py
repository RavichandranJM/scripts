#! /usr/bin/python

import requests
from bs4 import BeautifulSoup as bs

soup = bs(requests.get("http://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture").text)
for row in soup.find_all('p'):
    print row.getText()
