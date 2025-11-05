#!/usr/bin/env python3

import sys

if len(sys.argv) !=3:
    raise SystemExit('Usage: NextBus.py route stopId')

route = sys.argv[1]
stopId = sys.argv[2]

import urllib.request

u = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getStopPredictions.jsp?route={}&stop={}'.format(route,stopId))
data = u.read()

from xml.etree.ElementTree import XML
doc = XML(data)
print(doc)

# import pdb; pdb.set_trace()         # lauch debugger

# for pt in doc.findall('.//pt'):
#     print(pt.text)