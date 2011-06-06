# -*- coding: utf-8 -*-

#guardar esse arquivo para estudos basicos e pra criar um tutorial no futuro...

import sys
import socket
import string

HOST="irc.freenode.net"
PORT=6667
NICK="yupana"
IDENT="kernelpanic"
REALNAME="yupana"
CHAN="#tupantapuia"
readbuffer=" "

s=socket.socket( )
s.connect((HOST, PORT))
s.send("NICK %s\r\n" % NICK)
s.send("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME))
s.send("JOIN :%s\r\n" % CHAN)
s.send("PRIVMSG %s :%s\r\n" % (CHAN, "Ola"))
s.send("PRIVMSG %s :%s\r\n" % (CHAN, "Eu sou Yupana. Meu código esta em https://github.com/glerm/yupana. Se precisar aprofundar sobre IRC, tente esse link: http://www.irchelp.org/irchelp/rfc/rfc.html"))

while 1:
	readbuffer=readbuffer+s.recv(1024)
	temp=string.split(readbuffer, "\n")
	readbuffer=temp.pop( )

	for line in temp:
		line=string.rstrip(line)
		line=string.split(line)

		if(line[0]=="PING"):
			s.send("PONG %s\r\n" % line[1])

		if(line[1]=="PRIVMSG"):
			l=line[3].split(':')+line[4:] #split do ponto e virgula so pra testar, bug se tentar fazer frases tipo "Seguinte: blablabla"
			s.send("PRIVMSG %s :%s\r\n" % (CHAN, "Você disse: "+" ".join(l[1:])))
		


		#print line #debug mode


