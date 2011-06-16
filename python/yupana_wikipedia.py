#!/usr/bin/python
# -*- coding: utf-8 -*-
# todas libs estão a uma googlada de distancia?
import sys
import urllib2
from stripogram import html2text
import random

#emabaralhador
def scramble(string):
	palavras=string.split()
	random.shuffle(palavras,random.random)
	return ' '.join([p for p in palavras])

#palavra chave
busca=sys.argv[1]

#lang=en ingles
#lang=pt portugues
#lang=el  grego
#lang-hi hindi
lang=sys.argv[2]


### mais sobre expressões regulares:
#<TAG\b[^>]*>(.*?)</TAG> - expressão regular pra tirar uma tag.
# http://www.pythonregex.com/

opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
infile = opener.open('http://'+lang+'.wikipedia.org/wiki/'+busca)
page = infile.read()


import re

html = page

pattern = re.compile('(?<=p>).+(?=</p)', re.DOTALL)

p=pattern.search(html).group()




text = html2text(p)



regex = re.compile("(.*?)(Contents|Índice|\[edit\]|\[editar\]|Πίνακας|\[Επεξεργασία\]|अनुक्रम|\[संपादित करें\])",re.DOTALL)
r = regex.search(text)

t=r.groups()

bio=t[0]


#sorte = scramble(bio)#embaralhador

print bio

