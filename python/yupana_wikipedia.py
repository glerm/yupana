#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import urllib2
from stripogram import html2text


#<TAG\b[^>]*>(.*?)</TAG> - expressão regular pra tirar uma tag.
# http://www.pythonregex.com/

opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
infile = opener.open('http://en.wikipedia.org/w/index.php?title='+sys.argv[1])
page = infile.read()


import re

html = page

pattern = re.compile('(?<=p>).+(?=</p)', re.DOTALL)

p=pattern.search(html).group()




text = html2text(p)

#regex = re.compile("(.*?)\[edit\]",re.DOTALL)
#r = regex.search(text)

#t=r.groups()

#texto=t[0]

regex = re.compile("(.*?)(Contents|Índice|\[edit\])",re.DOTALL)
r = regex.search(text)

t=r.groups()

print t[0]

