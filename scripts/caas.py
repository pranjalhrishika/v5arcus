#!/usr/bin/python2
import commands
import cgi
import re
import os
import Cookie

print "Content-Type: text/html"

#print "<h1>running your cmd command</h1>"
a= commands.getoutput("sudo docker images")

b = a.splitlines()
i=0
l=len(b)
c=[]
d=[]
while i < l:
        t=" ".join(b[i].split())
        c.append(t)
        d.append(c[i].split(" "))
        i+=1
tot=cgi.FormContent()['n'][0]
print "set-cookie: total={}".format(tot)
print 
print "<center>"
print "<h2>---- Launch your containers here ----</h2>"
print "<form action='docker-launch.py'>"
print "<h3>"
i=1
while i<= int(tot) :
	print "enter name for container-{0} <input type='text' name='con{0}' />".format(i)
	print "select operating system"
	print "<select name='image{}'>".format(i)
	j=1
	l=len(d)
	while j< l:
	        print "<option>{}:{}</option>".format(d[j][0],d[j][1])
        	j+=1
	print "</select>"
	print "<br /><br />"
	i+=1
print "</h3>"	
print "<input type='submit' />"
print "</form>"
print "</center>"
