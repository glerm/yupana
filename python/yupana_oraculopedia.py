#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import urllib2
from stripogram import html2text
import random
import re
from yupanatwitta import *


# busca=[(meme,lingua),(...)] pt(portugues), el (grego), hi (hindi) ou en (ingles), mas da pra implemntar mais mexendo na expressã regular regex, mais abaixo
busca=[('Alchemy','en'),('Eclipse','pt'),('Vida','pt'),('Turing_Test','en'),('Oráculo','pt'),('Curupira','pt'),('Μαντείο','el'),('Ποίηση' ,'el'),('नैतिकता', 'hi'),('मनोविज्ञान','hi')]

brain='' #inicializando cerebro

letras=140 #limite de caracteres


### mais sobre expressões regulares:
#<TAG\b[^>]*>(.*?)</TAG> - expressão regular pra tirar uma tag da uma ideia de como cortar trechos
# http://www.pythonregex.com/

for b in busca:
	opener = urllib2.build_opener()
	opener.addheaders = [('User-agent', 'Mozilla/5.0')]
	infile = opener.open('http://'+b[1]+'.wikipedia.org/wiki/'+b[0])
	page = infile.read()
	html = page
	pattern = re.compile('(?<=p>).+(?=</p)', re.DOTALL)
	p=pattern.search(html).group()
	text = html2text(p)
	regex = re.compile("(.*?)(Contents|Índice|\[edit\]|\[editar\]|Πίνακας|\[Επεξεργασία\]|अनुक्रम|\[संपादित करें\])",re.DOTALL)
	r = regex.search(text)
	t=r.groups()
	bio=t[0]
	brain=brain+bio


sorte = scramble(brain)#embaralhador
sorte = "#wiqua "+sorte
sorte = sorte[:letras]
sorte = scramble(sorte)


print sorte

