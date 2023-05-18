#!/usr/bin/env python
# coding: utf-8


import pymysql
import cgi
import cgitb
import json

cgitb.enable()

form = cgi.FieldStorage()

print("Content-type: text/html\n")

def executeQuery(query, params):
  connection = pymysql.connect(
     host='bioed.bu.edu',
     user="soueryw",
     password="soueryw",
     db="Team_G",
     port = 4253)
  cursor = connection.cursor()
  try:
     cursor.execute(query,params)
  except pymysql.Error as e:
     print(e)
  results = cursor.fetchall()
  connection.commit()
  return(results)

if form:
  query = form.getvalue("query","")
  if (query == "wholePatientSearch"):
    option = form.getvalue("opt","")
    if (option == "option 1"):
      query1 = """
              select * from Persons where PersonID = 1
                """
      multiOut = executeQuery(query1)
      if (len(multiOut) == 0):
          print(json.dumps({'error': 1, 'message': "There was no data for the option %s" % (option)}))
      else:
          print(json.dumps({'error': 0,'table_data':multiOut}))
    elif (option == "option 2"):
        query2 = """
                select * from Persons where PersonID = 2
                """
        multiOut = executeQuery(query2)
        if (len(multiOut) == 0):
          print(json.dumps({'error': 1, 'message': "There was no data for the option %s" % (option)}))
        else:
          print(json.dumps({'error': 0,'table_data':multiOut}))
    else:
        query3 = """
                select * from Persons where PersonID = 3
                """
        multiOut = executeQuery(query3)
        if (len(multiOut) == 0):
          print(json.dumps({'error': 1, 'message': "There was no data for the option %s" % (option)}))
        else:
          print(json.dumps({'error': 0,'table_data':multiOut}))

