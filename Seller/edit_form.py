#!C:/Users/jim11/anaconda3/python.exe
# -*- coding: utf-8 -*-
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import cgi
from db import conn, cur





form = cgi.FieldStorage() 
ID = int(form.getvalue('id'))
if ID <= 0:
    print("Content-type: text/html\n")
    print("Error!! Empty ID")
    exit(0)

sql = "SELECT name, description, price FROM seller WHERE id = %s;"
cur.execute(sql, (ID,))  
name, description, price = cur.fetchone()

print("Content-type: text/html\n")
print(f"""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">

<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Shipping car</title>
</head>
<body>

<form id="myForm" method="post">
    <input name="prd_id" type="hidden" value="{ID}"/>
    Product name: <input name="prd_name" type="text" value="{name}" /><br/>
    <br/>

    <div style="display: grid; grid-template-rows: auto auto;">
    <label for="prd_description">Bewrite:</label>
    <textarea name="prd_description" id="prd_description">{description}</textarea>
    </div>

    <br/>
    Fixed price: <input name='prd_price' type='text' value="{price}" /><br>
    <hr/>
    <input type='button' onClick="postForm('edit')" value="send-out">
</form>

</body>
</html>
""")
