#!/usr/bin/python
# -*- coding: utf-8 -*-

import twitter
import random

def scramble(string):
	palavras=string.split()
	random.shuffle(palavras,random.random)
	return ' '.join([p for p in palavras])


api = twitter.Api(consumer_key='mEaddK449z4IPPSkZHmjKg',consumer_secret='3etNFlnaa3YziIoZw4hLdQJHOpPVqBs97EEiWWfTIw', access_token_key='316915236-00r1KH7wOQwX106FxhigEpkizo97oqhYyD6XZi8Q', access_token_secret='g3KJLK1qBfyhtBGC0N42B6UdoK7bCUYJpoTwezTzhU') 

#status = api.PostUpdate('Uma frase sensível e bem formada, bem aqui? Assim ritmo segredo logos exterioridade ')

frase=' '

#busca = api.GetSearch('devir',lang='pt') + api.GetSearch('animal',lang='pt') + api.GetSearch('vertigem',lang='pt') + api.GetSearch('labirinto',lang='pt')+ api.GetSearch('lua',lang='pt') + api.GetSearch('teste+de+turing',lang='pt') + api.GetSearch('tecnomagia',lang='pt')+ api.GetSearch('besta',lang='pt') + api.GetSearch('oraculo',lang='pt')

busca = api.GetUserTimeline('dasilvaorg')+api.GetUserTimeline('glerm')+api.GetUserTimeline('foucault')+api.GetUserTimeline('nietzsche')+api.GetUserTimeline('deluze')+api.GetUserTimeline('bailux')+api.GetUserTimeline('leminski')+api.GetUserTimeline('noishx')+api.GetUserTimeline('passars')+api.GetUserTimeline('filosonia')+api.GetSearch('oraculo',lang='pt')+api.GetSearch('#wiqua',lang='pt')+api.GetSearch('caos',lang='pt')


for b in busca:
	frase=frase+b.text

frase = scramble(frase)

print frase[:439]





#[b.text for b in busca]
