#!/usr/bin/python2

import cgi
import commands

print "Content-Type: text/html"
print
print "hello"
user=cgi.FormContent()['user'][0]
paswd=cgi.FormContent()['paswd'][0]
ip=cgi.FormContent()['ip'][0]
vg=cgi.FormContent()['vg'][0]
clientpass=cgi.FormContent()['clientpass'][0]
clientip=cgi.FormContent()['clientip'][0]
size=cgi.FormContent()['size'][0]

write="""[storageserver]
{0}   ansible_ssh_user=root  ansible_ssh_pass={1}

[webserver]
192.168.43.85   ansible_ssh_user=root  ansible_ssh_pass=redhat1

[clientserver]
{2}   ansible_ssh_user=root  ansible_ssh_pass={3}
""".format(ip,paswd,clientip,clientpass)



f2=open("/webcontent/ansible/hosts",'w')
f2.write(write)
f2.close()


#print user
#print paswd

write1="""---
- hosts: storageserver
  tasks:

        - package:
                         name: "scsi-target-utils.x86_64"
                         state: present

        - file:
                         state: directory
                         path: "/gbs"

        - fetch:
                         src: "/etc/tgt/targets.conf"
                         dest: "/gbs/"
                         flat: yes

        - lvol:
                         vg: "{0}"
                         lv: "{1}"
                         size: "{2}"
                          
- hosts: webserver
  tasks:
        - file:
                         path: "/gbs/targets.conf"
                         owner: "apache"

        - blockinfile:
                         path: "/gbs/targets.conf"
                         block:  |
                           <target {1}>
                               backing-store /dev/{0}/{1}
                           </target>

- hosts: storageserver
  tasks:
        - copy:
                         src: "/gbs/targets.conf"
                         dest: "/etc/tgt/targets.conf"



        - service:
                         name: "tgtd"
                         state: restarted

- hosts: clientserver
  tasks:
        - open_iscsi:
                         show_nodes: yes
                         discover: yes
                         portal: {3}
                         login: yes
                         target: {1}



""".format(vg,user,size,ip)

f1=open("/webcontent/ansible/part1.yml",'w')
f1.write(write1)
f1.close()

#print "<pre>"
a= commands.getstatusoutput("sudo ansible-playbook ../ansible/part1.yml -i ../ansible/hosts")
#print "</pre>"
print a.split('\n')
print "<br /><br /><br /><br />"

print "Block storage set up successfully"

