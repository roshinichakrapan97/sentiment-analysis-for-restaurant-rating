#!C:\Python36\python
#!C:\Python36\python
from flask import Flask,session,request
import cgi
import cgitb
import mysql.connector
import smtplib
print ("Content-type: text/html")
print()
print("<html>")
print("<head>")
print("<link href='master.css' rel='stylesheet'>")
print("<link href='share.css' rel='stylesheet'>")
print("<title> The Tasty Spoon</title>")
print("<header><h1>Suggestions</h1></header>")

print("</head>")

print("<body>")
print("<nav>")
print("<a href='search.html'> HOME</a><br><br>")
print("<a href='reviews.html'> BACK</a><br><br>")
print("</nav>")
form = cgi.FieldStorage()

rest_name=form.getvalue("res")
user = form.getvalue("user")
com=form.getvalue("review")
sender = 'vaidhehi.vasudevan@gmail.com' 
#receivers = mail
receivers='roshinivcp@gmail.com'
message = "From: From TASTY SPOON \nTo: To ADMIN <%s> \nSubject: SUGGESTING A NEW RESTAURANT\nThis suggestion is from the user %s for the restaurant %s. \nDETAILS:%s"%(receivers,user,rest_name,com)
#(,user,rest_name,com)
#message = "From: From TASTY SPOON \nTo: To ADMIN <%s>\nSubject: SUGGESTING A NEW RESTAURANT.\nThis suggestion is from the user %s for the restaurant %s \nDETAILS: %s"%(receivers,user,rest_name,com)
#message = "hi"
try:
        smtpObj = smtplib.SMTP('smtp.gmail.com',587)
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.login("vaidhehi.vasudevan","bourbon14")
        smtpObj.sendmail(sender, receivers , message)
        print("<br><br>")
        print ("<b><i><h3 style='color:maroon;font-family:Times New Roman;'>&nbsp&nbsp&nbsp&nbspTHANKS FOR YOUR SUGGESTION - WE WILL ADD THE RESTAURANT SOON</i></b> </h3><br>")
        #print("Thanks for your suggestion")
	#print("<b><i><h3 style='color:maroon;font-family:Times New Roman;'>&nbsp&nbsp&nbsp&nbsp {} THANKS FOR YOUR SUGGESTION - WE WILL ADD THE RESTAURANT SOON  </i></b> </h3><br>".format(user))
except SMTPException:
   print ("Error: unable to send email")


    
print("</body>")
print("</html>")
