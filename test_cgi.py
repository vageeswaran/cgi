#!"C:\Python27\python.exe"
print "Content-type: text/html"
print
print """<html>
<title>Test CGI</title>
<body>
<form enctype="multipart/form-data" action="fileup.py" method="post" >
File: <input type="file" name="file"><br />
<input type="submit" value="Submit" />
</form>
</body>
</html>
"""
