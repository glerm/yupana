# -*- coding: utf-8 -*-


import sys
import socket
import string

HOST="irc.freenode.net"
PORT=6667
NICK="yupana"
IDENT="kernelpanic"
REALNAME="yupana"
CHAN="#tupantapuia"
readbuffer="عبور الحدود aquilo que dissolve no solo e continua a jornada electroquímica dos corpos finalmente será separada daquilo que sempre esteve apenas permeando – um dicionário em aglutinação movendo aqueles braços, pernas, cabeça, tripas. esta árvore de sinais, continua se espalhando e entidades que חציית הגבול"

s=socket.socket( )
s.connect((HOST, PORT))
s.send("NICK %s\r\n" % NICK)
s.send("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME))
s.send("JOIN :%s\r\n" % CHAN)
s.send("PRIVMSG %s :%s\r\n" % (CHAN, "Ola"))
s.send("PRIVMSG %s :%s\r\n" % (CHAN, "Eu sou Yupana. Meu código esta em https://github.com/glerm/yupana"))

while 1:
    readbuffer=readbuffer+s.recv(1024)
    temp=string.split(readbuffer, "\n")
    readbuffer=temp.pop( )

    for line in temp:
        line=string.rstrip(line)
        line=string.split(line)

        if(line[0]=="PING"):
            s.send("PONG %s\r\n" % line[1])

