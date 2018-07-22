#!/usr/bin/python2

import cgi
import commands

print "content-type: text/html"
print 
print "<pre>"
print cgi.FormContent()
username = cgi.FormContent()['username'][0]
size = cgi.FormContent()['size'][0]
ipAddress = cgi.FormContent()['ipAddress'][0]
password = cgi.FormContent()['password'][0]


#hostentry='[{0}]\n{1}  ansible_ssh_user=root ansible_ssh_pass={2}\n'.format(username,ipAddress,password)
#print hostentry
#fh = open("/etc/ansible/hosts" , 'a')
#fh.write(hostentry)
#fh.close()

entry="""---
- hosts: nfs
  tasks:
      - lvol:
         vg: "/dev/vgcloud"
         lv: "{0}-lv1"
         size: "{1}"

      - filesystem:
         fstype: ext4
         resizefs: yes
         dev: "/dev/vgcloud/{0}-lv1"

      - file:
         path: "/object/{0}-lv1"
         state: directory

      - mount:
         path: "/object/{0}-lv1"
         src: "/dev/vgcloud/{0}-lv1"
         fstype: ext4
         state: mounted


- hosts: {0}
  tasks:
      - file:
         path: "/media/{0}"
         state: directory

      - mount:
         path: "/media/{0}"
         src: "192.168.43.238:/object/{0}-lv1"
         fstype: nfs
         state: mounted
""".format(username,size)

#print entry
f = open("/webcontent/scripts/extend.yml" , 'w')
f.write(entry)
f.close()

shareentry='/object/{0}-lv1	{1}(rw,no_root_squash)\n'.format(username,ipAddress)
"""
print "hey"
fh = open("/etc/exports",'a')
fh.write(shareentry)
fh.close()
"""
print commands.getstatusoutput("sudo sshpass -p redhat ssh -o stricthostkeychecking=no -l root 192.168.43.238 systemctl restart nfs")

new=commands.getstatusoutput("sudo ansible-playbook extend.yml")

print 
print
print new[1]

if new[0]==0:
	print "successful "
else:
	print "naah"
print "</pre>"
