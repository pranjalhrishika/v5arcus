#!/usr/bin/python2

import cgi
import commands

print "content-type: text/html"
print

username = cgi.FormContent()['username'][0]


print "<center><pre>"
print commands.getoutput("sudo sshpass -p redhat ssh -o stricthostkeychecking=no -l root 192.168.43.238 lvdisplay /dev/vgcloud/{0}-lv1".format(username))
print "</pre></center>"


print """

<!DOCTYPE html >
<head>
<title>Untitled Document</title>

 <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
 <style>
.log-btn {
  background: #FFFFFF;
  dispaly: inline-block ;
  width: 34%;
  font-size: 16px;
  height: 30px;
  color: #1e90ff;
  margin-left:120px;
  text-decoration: none;
  border: none;
   border-radius: 4px;
}

</style>
</head>

<body>




<div class="row" >
  <div class="col-md-3">
  </div>
  
  <div class="col-md-6" style="border:solid #CC6600 7px;height : auto;background-color: #1e90ff; margin-top:50px ">
  <table style="border:#1e90ff; solid 1Px;">
   <tr>
     <td style=" height:300px;background-color: #1e90ff;"> 
     <div style="  margin-left:12% ">  
     <FORM name="fillform" style="background-color: #1e90ff; width: 550px;height:auto;  padding: 40px 30px; " action="extend.py" >
      <table border="0" >
      <tr>
      <td style="height:50px;font-size:16px; color:#FFFFFF"><b>Re-enter your Username:</TD>
      <td style="height:50px"><INPUT TYPE="TEXT"  NAME="username" SIZE="26" placeholder='enter username' style="border: none;padding: 5px 7px 5px 15px;background:#fff;
	  color:#666;border:2px solid #ddd;margin-left:15px;    border-radius: 4px; line-height:10px; ">
          <label id="err1" style="color:#F00"></label>
      </td>
      </tr>
      <tr>
      <td style="height:50px; font-size:16px; color:#FFFFFF"><b>Enter your IP Address:</TD>
      <td style="height:50px"><INPUT TYPE="text"  NAME="ipAddress" placeholder='eg. 192.168.0.0' SIZE="26" style="border: none;padding: 5px 7px 5px 15px;background:#fff;
	  color: #666;border:2px solid #ddd; margin-left:15px;     border-radius: 4px; line-height:10px;">
       <label id="err2" style="color:#FF0000"></label>
      </td>
      </tr>	 
	  <tr>
      <td style="height:50px;font-size:16px; color:#FFFFFF"><b>Enter size to extend (in MB):</TD>
      <td style="height:50px"><INPUT TYPE="text" NAME="size" placeholder='eg. 1024, 512' SIZE="26" style="border: none;padding: 5px 7px 5px 15px;background:#fff;
	  color: #666;border:2px solid #ddd; margin-left:15px;     border-radius: 4px; line-height:10px;">
       <label id="err2" style="color:#FF0000"></label>
      </td>
      </tr>	 
	  <tr>
      <td style="height:50px;font-size:16px; color:#FFFFFF"><b>Enter Password: </TD>
      <td style="height:50px"><INPUT TYPE="password"  NAME="password" placeholder='enter password' SIZE="26" style="border: none;padding: 5px 7px 5px 15px;background:#fff;
	  color: #666;border:2px solid #ddd; margin-left:15px;     border-radius: 4px; line-height:10px;">
       <label id="err2" style="color:#FF0000"></label>
      </td>
      </tr>	 
  </table>
  <br />
    <input type="submit"  class="log-btn" />
    </FORM> 
    </div>
   </td>
   </tr>
 </table>
  </div>
  
  <div class="col-md-3">
  </div>
  
</div>

</body>
</html>

"""
