#!/usr/bin/python2
import cgi
import commands

print "content-type: text/html"
print 
x='0'
y='0'
z='0'
w='0'
a='0'
d=cgi.FormContent()
dname=cgi.FormContent()['dname'][0]
version=cgi.FormContent()['ver'][0]
ImageName=cgi.FormContent()['image'][0]
#print dname
#print version
#print ImageName
for i in d.keys():
	if d[i][0]=="ssh":
		x="ssh"
	elif d[i][0]=="httpd":
                y="httpd"
        elif d[i][0]=="net":
                z="ntool"
        elif d[i][0]=="python":
                w="python"
	elif d[i][0]=="nfs":
		a="nfs"
commands.getoutput("sudo cat > /commit/Dockerfile")
commands.getoutput("sudo chown apache /commit/Dockerfile")
if ImageName == "centos":
   commands.getstatusoutput("echo 'FROM centos' | sudo cat >> /commit/Dockerfile")
if x == "ssh":
   commands.getoutput("echo 'RUN yum install openssh -y' | sudo cat >> /commit/Dockerfile")
if y == "httpd":
   commands.getoutput("echo 'RUN yum install httpd -y' | sudo cat >> /commit/Dockerfile")
if z == "ntool":
   commands.getoutput("echo 'RUN yum install net-tools -y' |sudo cat >> /commit/Dockerfile")
if a == "nfs":
   commands.getoutput("echo 'RUN yum install nfs-utils -y' |sudo cat >> /commit/Dockerfile")
if w == "python":
   commands.getstatusoutput("echo 'RUN yum install python2 -y' | sudo cat >> /commit/Dockerfile")

commands.getoutput("sudo docker build -t {0}:{1} /commit".format(dname,version))
commands.getoutput("rm -rf /commit/Dockerfile")
print "<pre>"
print commands.getoutput("sudo docker images {0}".format(dname))
print "</pre><br>"
print "<a href='caashome.py'>Go Back</a>"


