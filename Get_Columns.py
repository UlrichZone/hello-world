#!/usr/bin/python
# -*- coding: <utf-8> -*-

info = []
raw_text = open( 'text.txt', 'r' )

for line in raw_text.readlines():
    cut = line.strip()
    cut = line.find('=')
    variables = line[0:cut-1]
    info.append(variables)

print(info)
