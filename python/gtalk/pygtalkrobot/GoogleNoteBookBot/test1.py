#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2

proxy_info = {
    'user' : "",
    'pass' : "",
    'host' : "web-proxy.hpl.hp.com",
    'port' : 8088
}

proxy_support = urllib2.ProxyHandler({"http" : "http://%(host)s:%(port)d" % proxy_info})

l_opener = urllib2.build_opener(proxy_support, urllib2.HTTPHandler)

urllib2.install_opener(l_opener)
l_req = urllib2.urlopen('http://www.google.com')
print l_req.headers
print l_req.read()
