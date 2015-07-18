#!"C:\Python27\python.exe"
import cgi,cgitb
import MySQLdb

db=MySQLdb.connect('127.0.0.1','root','','test')
cur=db.cursor()
form=cgi.FieldStorage()
fname=form.getvalue('fname')
lname=form.getvalue('lname')
sql="""insert into details values("%s","%s")"""%(fname,lname)
cur.execute(sql)
db.commit()
print "Content-type: text/html"
print
print "<title>Test CGI</title>"
print """<h2>hello %s %s</h2>"""%(fname,lname)

