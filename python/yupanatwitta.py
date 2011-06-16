#!/usr/bin/python
# -*- coding: utf-8 -*-

import twitter
import random

def scramble(string):
	palavras=string.split()
	random.shuffle(palavras,random.random)
	return ' '.join([p for p in palavras])


def twitta(string):
	api = twitter.Api(consumer_key='mEaddK449z4IPPSkZHmjKg',consumer_secret='3etNFlnaa3YziIoZw4hLdQJHOpPVqBs97EEiWWfTIw', access_token_key='316915236-00r1KH7wOQwX106FxhigEpkizo97oqhYyD6XZi8Q', access_token_secret='g3KJLK1qBfyhtBGC0N42B6UdoK7bCUYJpoTwezTzhU') 
	status = api.PostUpdate(string)





