#!/usr/bin/python2

import cgi
import commands

print"content-type: text/html" 
print
#print cgi.FormContent()

code=cgi.FormContent()['code'][0]
lang=cgi.FormContent()['lang'][0]
print "\n\n\n" 
print "<pre>"
if lang == 'c':
	f=open("/webcontent/scripts/cprog.c",'w')
        f.write(code)
        f.close()
	commands.getstatusoutput("sudo gcc cprog.c -o cprog")
	commands.getstatusoutput("sudo chown apache cprog")
	print commands.getoutput("./cprog")
	commands.getoutput("sudo rm -rf cprog")

elif lang == 'pythontwo':
	
	f=open("/webcontent/scripts/pythcode.py",'w')
	f.write(code)
	f.close()
	print commands.getoutput("sudo python pythcode.py")

print "</pre>"
#print a
#print code

