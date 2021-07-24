#! /usr/bin/env python

import cgi

reshtml = """ Content-Type : text/html\n
<html><head><title>
Friends CGI Dynamic Script
</title></head>
<body><h3> Friends List for : <i>%s</i></h3>
Your name is : <b> %s </b>
You have : <b> %s </b> friends
</body></html>
"""
formObj = cgi.FieldStorage()
who = formObj['person'].value
friends = formObj['howmany'].value
print reshtml % (who, who, friends)
