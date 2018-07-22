#!/usr/bin/python2
import cgi
import commands
import os
import Cookie

print "content-type: text/html"
print

print """
<script>
function rm(mycname)
{
document.location='docker_remove.py?x=' + mycname;
}

function stop(mycname)
{
document.location='docker_stop.py?x=' + mycname;
}

function start(mycname)
{
document.location='docker_start.py?x=' + mycname;
}

</script>
"""

l=Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
total=l["total"].value
print "<center>"
print "<pre>"
print
if int(total)<=0:
	print "<h2> Go back and Launch your container </h2>"
	print "<h3><a href='caashome.py'>GO CaaS Home</a></h3>"
else:
	print "<h1>--- LIST OF LAUNCHED CONTAINER ---</h1>"
	a=commands.getoutput("sudo docker ps -a -n {0}".format(total))
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
	print "<tr><th>Container_NAME </th><th>Image_NAME:version</th><th>IP_Address</th><th>STATUS</th><th>START</th><th>STOP</th><th>REMOVE</th></tr>"
	i=1
	l=len(d)
	while i< l:
		ipstatus=commands.getoutput("sudo docker inspect {0} | jq '.[].NetworkSettings.Networks.bridge.IPAddress'".format(d[i][-1]))
		status = commands.getoutput("sudo docker inspect {0} | jq '.[].State.Status'".format(d[i][-1]))
		print "<tr><th>"+ d[i][-1] + "</th><th>" + d[i][1] +"</th><th>"+ ipstatus +"</th><th>"+ status +"</th><td> <input value='" + d[i][-1]    +  "' type='button' onclick=start(this.value)  />   </td><td>  <input value='" + d[i][-1]    +  "' type='button' onclick=stop(this.value)  /> </td><td>  <input value='" + d[i][-1]  +  "' type='button' onclick=rm(this.value)  /> </td></tr>"
		i+=1
	print "</h2>"
	print "</table>"
	print "<hr />"
	print "</pre>"
	print "<form action='docker-work.py'>"
	print "Enter container name to Launch a live Shell   <input type='text' name='conname'>"
	print "<input type='hidden' name='work' value='shell'>"
	print "<input type='submit'>"

print "</center>"

