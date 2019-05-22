#Домашная работа урок 15

#Просьба проверить предыдущее домашнее задание https://github.com/iq321/Lesson-14-homework

# 1)Вывести покупателей (полное имя, номер телефона) которые что либо покупали, проживающих в одном городе, если их кол-во в городе больше 1.
# 2)Вывести топ 3 самых платежеспособных города за все время.
# 3)Вывести самый популярный, на основании кол-ва продаж, жанр (название) и все треки в нем (название, альбом, исполнитель).

import sqlite3 as lite
import pprint
import pickle
import sys

#def task1():
  # В процессе решения

def task2():
  try:
    con = None
    con = lite.connect('Chinook_Sqlite.sqlite')
    query_string = '''
      SELECT Customer.City, SUM(Total)
      FROM Customer   
      INNER JOIN Invoice ON Customer.CustomerID = Invoice.CustomerID
      GROUP BY Customer.City
      ORDER BY SUM(Total) DESC 
      LIMIT 3             
      '''
    cur = con.cursor()
    cur.execute(query_string)
    pprint.pprint(cur.fetchall())
  except Exception as e:
    print(e)
    sys.exit(1)
  finally:
    if con is not None:
      con.close()

#def task3():
  # В процессе решения

task2()