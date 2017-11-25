#!/usr/bin/python

import urllib.request
import json

resp = urllib.request.urlopen('https://httpbin.org/ip')
data = json.load(resp)
print(data['origin'])
