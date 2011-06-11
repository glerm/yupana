# -*- coding: utf-8 -*-

import aiml

bot=aiml.Kernel()

bot.learn("yupana.aiml")

while True:
	input=raw_input("pense: ")
	response=bot.respond(input)
	print response



