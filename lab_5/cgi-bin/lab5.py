#!/usr/bin/python3
import random
import cgi
import cgitb

print("Content-type: text/html; charset=utf-8\r\n\r\n")
html = """<html>
<head>
<title>Response</title>
<link rel="shortcut icon" href="">
</head>
<body>"""

numbers = []
for i in range(16):
    rand = random.randint(-33, 44)
    numbers.append(rand)


def group1(numbers):
    count = 0
    for i in numbers:
        if i >= 0:
            count += i
    return count


def group2(numbers):
    list_min = []
    for i in numbers:
        if i < 0:
            list_min.append(i)
    max_num = max(list_min)
    return max_num


def group3(numbers):
	sort_list = sorted(numbers, key=abs)
	return sort_list


form = cgi.FieldStorage()
name_user = form.getfirst("name_user")
func1 = form.getfirst("func1")
func2 = form.getfirst("func2")
func3 = form.getfirst("func3")

html += "<p>16 случайных чисел в диапазоне (-33; 44):</p>"
html += f"<p>{', '.join([str(el) for el in numbers])}</p>"
html += "<p>Результаты:</p>"
if func1:
    html += "<p>Сумма положительных чисел: " + str(group1(numbers)) + "</p>"
if func2:
    html += "<p>Максимальное число среди отрицательных чисел: " + str(group2(numbers)) + "</p>"
if func3:
    html += "<p>Сортировка чисел, взятых по абсолютной величине: " + ", ".join([str(el) for el in group3(numbers)]) + "</p>"
html+= "</body>"
print(html)


