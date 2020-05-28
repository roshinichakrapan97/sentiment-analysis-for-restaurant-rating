#!C:\Python36\python
#!C:\Python36\python
from flask import Flask,session,request
import cgi
import cgitb
import mysql.connector
print ("Content-type: text/html")
print()
print("<html>")
print("<head>")
print("<link href='master.css' rel='stylesheet'>")
print("<link href='share.css' rel='stylesheet'>")
print("<title> The Tasty Spoon</title>")
print("<header><h1>The Tasty Spoon</h1></header>")
print("<style>")
#print("header")
#print("{")
#print("display:block;")
#print("background-color:black;")
#print("width:100%;")
#print("padding:1.0em;")
#print("}")
#header h1{font-family:Comic Sans MS;color:maroon;line-height:10px;color:goldenrod;margin-left:5%;}
#print("small{font-family:arial;color:grey;}")
#print("body{margin:0em;background-image:url('drink1.jpg');")background-repeat: no-repeat;background-attachment: fixed;background-position: stretch;background-color: white; }")

print("</style>")
print("</head>")

print("<body>")
form = cgi.FieldStorage()
#rest_name = form['restaurant'].value
#loc=form['location'].value

#if request.method == 'POST':
#	restaurant=request.form['restaurant']
#if 'restaurant' in session:
#	rest_name=session['restaurant']

rest_name=form.getvalue("restaurant")
loc = form.getvalue("location")

#rest_name='a2b'
#loc='madipakkam'


cnx = mysql.connector.connect(user='root',password='',host='127.0.0.1',db='cip')
cur = cnx.cursor()

sql="select * from restaurant where r_name='%s' and r_loc='%s'"%(rest_name,loc)
cur.execute(sql)
for row in cur.fetchall():
	#val0=row[0]
	val1=row[1]	#name
	val2=row[2]	#number
	#val3=row[3]	
	val4=row[4]	#location
	val5=row[5]	#address
	val6=row[6]	#timing
	val7=row[7]	#menu0
	val8=row[8]	#menu1
	val9=row[9]	#menu2
	val10=row[10]	#famousitem
	val11=row[11]	#costfor2
	val12=row[12]	#rating
	val13=row[13]	#amb0
	val14=row[14]	#amb1
	val15=row[15]	#amb2

print("<nav>")

print("<a href='search.html'> BACK</a><br><br>")
print("</nav>")


print("<b><i><h3 style='color:maroon;font-family:Times New Roman;'>&nbsp&nbsp&nbsp&nbsp Name : %s"%val1+"</i></b> </h3><br>")
print("<b><i><h3 style='color:maroon;font-family:Times New Roman;'>&nbsp&nbsp&nbsp&nbsp Location : %s"%val4+"</i></b> </h3><br>")
print("<b><i><h3 style='color:maroon;font-family:Times New Roman;'>&nbsp&nbsp&nbsp&nbsp Address :%s"%val5+"</i></b> </h3><br>")
print("<b><i><h3 style='color:maroon;font-family:Times New Roman;'>&nbsp&nbsp&nbsp&nbsp Contact :%s"%val2+"</i></b> </h3><br>")
print("<b><i><h3 style='color:maroon;font-family:Times New Roman;'>&nbsp&nbsp&nbsp&nbsp Open at : %s"%val6+"</i></b> </h3><br>")
print("<b><i><h3 style='color:maroon;font-family:Times New Roman;'>&nbsp&nbsp&nbsp&nbsp Cost for two : %s"%val11+"</i></b> </h3><br>")
print("<b><i><h3 style='color:maroon;font-family:Times New Roman;'>&nbsp&nbsp&nbsp&nbsp Famous Dish: %s"%val10+"</i></b> </h3><br>")
print("<b><i><h3 style='color:maroon;font-family:Times New Roman;'>&nbsp&nbsp&nbsp&nbsp Rating: %s"%val12+"</i></b> </h3><br>")


menu0="%s"%val7+".jpg"
menu1="%s"%val8+".jpg"
menu2="%s"%val9+".jpg"




amb0="%s"%val13+".jpg"
amb1="%s"%val14+".jpg"
amb2="%s"%val15+".jpg"


print("<br>")
print("<h1><p align='center'><b><font color='purple'>MENU</font></b></p></h1>")
print("<img src='pic/{}' style='width:320px; height:320px'>".format(menu0))
print("<img src='pic/{}' style='width:320px; height:320px'>".format(menu1))
print("<img src='pic/{}' style='width:320px; height:320px'>".format(menu2))

print("<br><br>")
print("<h1><p align='center'><b><font color='purple'>AMBIENCE</font></b></p></h1>")
print("<img src='pic/{}' style='width:320px; height:320px'>".format(amb0))
print("<img src='pic/{}' style='width:320px; height:320px'>".format(amb1))
print("<img src='pic/{}' style='width:320px; height:320px'>".format(amb2))


print("<br><br>")
print("<h1><p align='center'><b><font color='purple'>REVIEWS</font></b></p></h1>")
print("<br>")
sql1="select * from comment where c_restaurant='%s'"%(rest_name)
cur.execute(sql1)
i=1
for row in cur.fetchall():
	#print("<br>")
	val_user=row[0]
	val_comment=row[2]
	print("<b><i><h3 style='color:maroon;font-family:Times New Roman;'>&nbsp&nbsp&nbsp&nbsp{}){} : {}</i></b></h3>".format(i,val_user,val_comment))
	i+=1
	



print("</body>")
print("</html>")