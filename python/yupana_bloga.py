# -*- coding: utf-8 -*-

#depende de https://github.com/maxcutler/python-wordpress-xmlrpc
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetRecentPosts, NewPost
from wordpress_xmlrpc.methods.users import GetUserInfo

wp = Client('http://yupana.pontaodaeco.org/xmlrpc.php', 'gesuselva', 'kernelpanic')


post = WordPressPost()
post.title = 'Que as atuais máquinas informacionais e comunicacionais não se contentem em veicular conteúdos representativos, mas que concorram igualmente para a confecção de novos agenciamentos de enunciação (individuais e/ou coletivos)?'
post.description = '<h1></h1><br><p>عبور الحدود aquilo que dissolve no solo e continua a jornada electroquímica dos corpos finalmente será separada daquilo que sempre esteve apenas permeando - <a href=\"https://github.com/glerm/yupana\"/>um dicionário em aglutinação movendo aqueles braços, pernas, cabeça, tripas.</a> esta árvore de sinais, continua se espalhando e entidades que חציית הגבול</p><img src=\"http://upload.wikimedia.org/wikipedia/commons/2/20/Boltzmanns-molecule.jpg\"/>'
post.tags = 'yupana, kernel'
post.categories = ['coding']
wp.call(NewPost(post, True))

