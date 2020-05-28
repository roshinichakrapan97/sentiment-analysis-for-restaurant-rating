import cgi
import cgitb
import smtplib
print ("Content-type: text/html")
print()
print("<html>")
print("<head>")
print("<link href='master.css' rel='stylesheet'>")
print("<link href='share.css' rel='stylesheet'>")
print("<title> The Tasty Spoon</title>")
print("<header><h1>The Tasty Spoon</h1></header>")

print("</head>")

print("<body>")
print("<nav>")
print("<a href='search.html'> HOME</a><br><br>")
print("<a href='reviews.html'> BACK</a><br><br>")
print("</nav>")
form = cgi.FieldStorage()

mail=form.getvalue("mail")
user = form.getvalue("user")
com=form.getvalue("review")


sender = 'vaidhehi.vasudevan@gmail.com' 
#receivers = mail
receivers='roshinivcp@gmail.com'
#message = "From: From Person <from@fromdomain.com>\nTo: To Person <to@todomain.com>\nSubject: SMTP e-mail test\nYour review has been added successfully"
message = "hi"
try:
   smtpObj = smtplib.SMTP('smtp.gmail.com',587)
   smtpObj.ehlo()
   smtpObj.starttls()
   smtpObj.login("vaidhehi.vasudevan","bourbon22")
   smtpObj.sendmail(sender, receivers , message)         
   print ("Successfully sent email")
except SMTPException:
   print ("Error: unable to send email")

   

print("</body>")
print("</html>")
