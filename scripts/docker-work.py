#!/usr/bin/python2
import commands
import cgi

print "Content-Type: text/html"
print

name=cgi.FormContent()['conname'][0]
work=cgi.FormContent()['work'][0]
print"<center>"
if work == 'shell':
	print "<br /><br />"
	print "<h3>shell prompt</h3>"
	print "<form action='docker-shell.py'>"
	print "<input type='hidden' name='cname' value='{}' />".format(name)
	print "<textarea cols='70' rows='10' name='code'>"
	print "</textarea>"
	print "<br />"
	print "<input type='submit'>"
	print "</form>"
	print "<a href='docker-manage.py'>go back</a>"	

elif work == 'server':
	print "<form action='docker-configure.py'>"
	print"<input type='hidden' name='cname' value='{}' />".format(name)
	print"""
	<input type='radio' name='conf' value='apache' />Apache Server
	<input type='radio' name='conf' value='nfs' />NFS Server
	<input type='radio' name='conf' value='ssh' />SSH Server
	<input type='submit' >

	</form>
	""" 
	print "<a href='docker-manage.py'>go back</a>"  
