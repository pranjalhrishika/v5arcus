#!/usr/bin/python2

import cgi
import commands

print "content-type: text/html"
print 

cmd=cgi.FormContent()['code'][0]
name=cgi.FormContent()['cname'][0]

print "<pre>" 
status= commands.getstatusoutput("sudo docker exec {} {}".format(name,cmd))
print status[1]
print "</pre>"
