#!/usr/bin/env python3
import cgi, cgitb
print("Content-Type: text/html\n")
print("<h3>Результаты тестирования</h3>")
form = cgi.FieldStorage()
name1 = form.getvalue("name1", "None")
data1 = form.getvalue("data1", "None")
data2 = form.getvalue("data2", "None")
data3 = form.getvalue("data3", "None")
data4 = form.getvalue("data4", "None")
data5 = form.getvalue("data5", "None")
print('Имя тестируемого:', name1)
#Вопрос №1
if data1=='3':
	print("<br>Ответ на вопрос 1 введен верно")
else:
	print("<br>Ответ на вопрос 1 введен неверно")
#Вопрос №1
#Вопрос №2
if data2=='1':
	print("<br>Ответ на вопрос 2 введен верно")
else:
	print("<br>Ответ на вопрос 2 введен неверно")
#Вопрос №2
#Вопрос №3
if data3=='3':
	print("<br>Ответ на вопрос 3 введен верно")
else:
	print("<br>Ответ на вопрос 3 введен неверно")
#Вопрос №3
#Вопрос №4
if data4=='2':
	print("<br>Ответ на вопрос 4 введен верно")
else:
	print("<br>Ответ на вопрос 4 введен неверно")
#Вопрос №4
#Вопрос №5
if data5=='1':
	print("<br>Ответ на вопрос 5 введен верно")
else:
	print("<br>Ответ на вопрос 5 введен неверно")
#Вопрос №5
print('')
print('''<br><br>Необоходимо сделать скриншот результатов и загрузить их
в электронную образовательную среду.''')