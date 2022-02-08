#!/usr/bin/python3

import cgi
import cgitb
import re

form = cgi.parse()

print("Content-type: text/html; charset=utf-8\r\n\r\n")
html = """<html>
<head>
<title>Response</title>
<link rel="shortcut icon" href="">
</head>
<body>"""

re_data1 = re.compile("^(Факультет) - [А-Яа-я0-9] + группа\. [А-Яа-я0-9]+$")
data1 = re_data1.match(form["data1"][0])

re_data2 = re.compile("^И.О. Фамилия [А-Яа-я0-9]+$")
data2 = re_data2.search(form["data2"][0])

data3 = re.match("^ЗК № [А-Яа-я0-9]+$", form["data3"][0])

data4 = re.search('''^\[\s{0,}['"].{0,}['"]\s{0,},\s{0,}\d{1,}\.\d{0,}\s{0,},\s{0,}(False|false|0|True|true|1)\s{0,}\]$''', form["data4"][0])
data = [data1 is None, data2 is None, data3 is None]
for boolean in data:
    if boolean:
    	html += "<p>Элемент формы не прошел проверки</p>"
    else:
        html += "<p>Элемент формы прошел проверку</p>"
if data4 is None:
    html += "<p>Литерал не прошел проверки</p>"
else:
    html += "<p>Литерал прошел проверку</p>"
html += "</body>"
print(html)


