#!/usr/bin/python2
import cgi
import commands
import os 
import Cookie
print "content-type: text/html"
print

a= cgi.FormContent()
l=len(a)
#print a

#l=Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
#total=l["total"].value

image_type=[]
container_name=[]
i=1
print "<center>"
print "<pre>"
print 
print "<h1><u>Your containers have been launched</u></h1><br />"
while i<=(l/2):
	x="c=cgi.FormContent()['con{}'][0]".format(i)
	exec(x)
	container_name.append(c)
	
	y="d=cgi.FormContent()['image{}'][0]".format(i)
        exec(y)
	image_type.append(d)	
	if commands.getstatusoutput("sudo docker inspect {}".format(container_name[i-1]))[0]==0:
		print "<h2>{0} : name already used,CONTAINER not launched</h2>".format(container_name[i-1])
		#tot=int(total)-1
	else:
		commands.getstatusoutput("sudo docker run -dit --name {0} {1}".format(container_name[i-1],image_type[i-1]))
	#print "<br />"
		print "<h2>{0}:CONTAINER launched </h2>".format(container_name[i-1])

	i+=1

#print tot
print "<a href='docker-manage.py'><h3>click here to manage your container</h3></a>"
print "</pre>"
print "</center>"

