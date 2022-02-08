#!/usr/bin/python3
import cgi
import cgitb
import os
cgitb.enable()
print("Content-type: text/html; charset=utf-8\r\n\r\n")
html = """<html>
<head>
<title>Response</title>
<link rel="shortcut icon" href="">
</head>
<body>"""
names = []
values = []
form = cgi.parse()
for el in form.keys():
	names.append(el)
for el in form.values():
	values.append(el[0])
path = "./CGI"
if not os.path.exists(path):
	os.mkdir(path)
os.chdir(path)
file_names = open("names.txt", "w")
file_names.write("\n".join(names))
file_values = open("values.txt", "w")
file_values.write("\n".join(values))
file_names.close()
file_values.close()
file_names = open("names.txt", "r")
file_values = open("values.txt", "r")
names_len = len(file_names.read())
html += "<p>Кол-во символов в файле names.txt (включая знак пустой строки): " + str(names_len) + "</p>"
values = file_values.readline()
values_len = len(values)
html += "<p>Кол-во символов в файле values.txt (включая знак пустой строки): " + str(values_len) + "</p>"
for el in values.split("\n"):
	html += "<p>" + str(el) + "</p>"
html += "</body>"
binary = open("./binary_data.dat", "w+b")
data = bytes(range(26))
binary.write(data)
binary.seek(20)
byte = binary.read(1)
binary.seek(-12, 1)
three_bytes = binary.read(1)
binary.close()
try:
	inp = int(form["input"][0])
	assert inp == 1
except Exception:
	print("Ошибка. Неверное число")
print(html)	

