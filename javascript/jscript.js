<script>
$(document).ready(function()
{  $("#alogindiv").hide();
$("#signupdiv").hide(); 
$("#ulogindiv").hide();  
$(".fancybox").fancybox();
 var scroll_start = 0;
  var startchange = $(".maintext");
  var offset = startchange.offset();

  if (startchange.length) {
    $(document).scroll(function() {
      scroll_start = $(this).scrollTop();
      if (scroll_start > offset.top) {
        $("#top").css('background-color', '#68c3a3');
      } else {
        $('#top').css('background-color', 'transparent');
      }
    });
  }
  });

function col()
{
var x=document.getElementById("topnav");
x.style.color="#68c3a3";
}
function colback()
{
var x=document.getElementById("topnav");
x.style.color="white";
}

function validation()
{ var username=document.fillform.uname.value;
  var ps=document.fillform.pwd.value;
  
    if(username=="")
  { document.getElementById("err1").innerHTML="!";
   var j=document.getElementById("uname1");
   j.style.border="thin solid red";
   return false;
  }
    if(ps=="")
  { document.getElementById("err2").innerHTML="!";
  var j=document.getElementById("pwd1");
   j.style.border="thin solid red";
  
  return false;
  } 
} 
function validationreg()
{ var fname2=document.regform.fname.value;
var lname2=document.regform.lname.value;
var gender2=document.regform.gender.value;
var date2=document.regform.date.value;
var emailid2=document.regform.emailid.value;
var password2=document.regform.password.value;
var cpassword2=document.regform.cpassword.value;
  
    if(fname2=="")
  { document.getElementById("err1").innerHTML="!";
   var j=document.getElementById("fname1");
   j.style.border="thin solid red";
   return false;
  }
    if(lname2=="")
  { document.getElementById("err2").innerHTML="!";
  var j=document.getElementById("lname1");
   j.style.border="thin solid red";
    return false;
  } 
  if(gender2=="")
  { document.getElementById("err3").innerHTML="!";
  var j=document.getElementById("gender1");
   j.style.border="thin solid red";
    return false;
  } 
  if(date2=="")
  { document.getElementById("err4").innerHTML="!";
  var j=document.getElementById("date1");
   j.style.border="thin solid red";
    return false;
  } 
  if(emailid2=="")
  { document.getElementById("err5").innerHTML="!";
  var j=document.getElementById("emailid1");
   j.style.border="thin solid red";
    return false;
  } 
  if(password2=="")
  { document.getElementById("err6").innerHTML="!";
  var j=document.getElementById("password1");
   j.style.border="thin solid red";
    return false;
  } 
   if(cpassword2=="")
  { document.getElementById("err7").innerHTML="!";
  var j=document.getElementById("cpassword1");
   j.style.border="thin solid red";
    return false;
  } 
} 

  
</script>
 