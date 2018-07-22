#!/usr/bin/python2

import commands
import cgi
import os 
import Cookie
print "content-type: text/html"
name= cgi.FormContent()['x'][0]
status=commands.getstatusoutput("sudo docker rm -f {0}".format(name))

l=Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
total=l["total"].value

if status[0] == 0:
	tot=int(total)-1
	print "set-cookie: total={}".format(tot)	       
	print "location:  docker-manage.py"
        print
else:
	print
        print "unable to removed"

