#!/usr/bin/python2
import commands
import cgi
import re
print "Content-Type: text/html"
print

#print "<h1>running your cmd command</h1>"
print "<center>"
print "<pre>"
print "<h1>--- WE HAVE THE FOLLOWING IMAGES ---</h1>"

a= commands.getoutput("sudo docker images")
b = a.splitlines()
i=0
l=len(b)
c=[]
d=[]

print "<table border='3'>"
while i < l:
        t=" ".join(b[i].split())
        c.append(t)
        d.append(c[i].split(" "))
        i+=1
print "<h2>"
print "<tr><th>Available Image</th><th>Version</th></tr>"
i=1
l=len(d)
while i< l:
	print "<tr><th>"+d[i][0] + "</th><th>" + d[i][1]+"</th></tr>"
        i+=1
print "</h2>"
print "</table>"
print "<hr />"

print """<form action='caas.py'>
<marquee><h2>Launch CONTAINERS of the available IMAGES</h2> </marquee>
<h4>enter no of container to launch<input type='number' name='n'>	<input type='submit'>
</h3>
</form>
"""
print "<h3>OR</h3>"
print "<h2>You can choose from the following PACKAGES and COMMIT your own DOCKER IMAGE</h2>"


print "<form action='docker-commit.py'>"
print "</pre>"
print "<h3>Select IMAGE</h3>"
print "<input type='radio' name='image' value='centos'>centos"
print "<br />"
print "<h3>-: Select PACKAGES :-</h3>"
print "</center>"
print """<pre>
<h3>
\t\t\t\t\t\t\t\t\t<input type='checkbox' name='soft1' value='httpd'>Apache Server
\t\t\t\t\t\t\t\t\t<input type='checkbox' name='soft2' value='ssh'>SSH Server
\t\t\t\t\t\t\t\t\t<input type='checkbox' name='soft3' value='net'>net-tools
\t\t\t\t\t\t\t\t\t<input type='checkbox' name='soft4' value='python'>python
\t\t\t\t\t\t\t\t\t<input type='checkbox' name='soft5' value='nfs'>NFS Server
</h3>
<center>
<h3>enter name for your image <input type='text' name='dname'>version<input type='text' name='ver'></h3>
<input type='submit'>
</center>
</pre>
</form>
"""
