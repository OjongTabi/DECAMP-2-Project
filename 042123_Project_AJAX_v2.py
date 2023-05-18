#!/usr/bin/env python
# coding: utf-8


import pymysql
import cgi
import cgitb
import json

cgitb.enable()

form = cgi.FieldStorage()

print("Content-type: text/html\n")

def executeQuery(query):
  connection = pymysql.connect(
     host='bioed.bu.edu',
     user="soueryw",
     password="soueryw",
     db="Team_G",
     port = 4253)
  cursor = connection.cursor()
  try:
     cursor.execute(query)
  except pymysql.Error as e:
     print(e)
  results = cursor.fetchall()
  connection.commit()
  return(results)

if form:
    query = form.getvalue("query","")
    if (query == "wholePatientSearch"):
        opt = form.getvalue("opt","")
        if (opt == "ETHN_GRP_CAT_TXT"):
            INPUT = 1 # UPDATE
            query1 = """
                select * from Persons 
                    """
            multiOut = executeQuery(query1)
            if (len(multiOut) == 0):
                print(json.dumps({'error': 1, 'message': "There was no data for your input: %s" % (opt)}))
            else:
                print(json.dumps({'error': 0,'table_data':multiOut}))
        elif (opt == "PERSON_GENDER"):
            INPUT = 2 # UPDATE
            query2 = """
                    select * from Persons 
                    """
            multiOut = executeQuery(query2)
            if (len(multiOut) == 0):
                print(json.dumps({'error': 1, 'message': "There was no data for your input: %s" % (opt)}))
            else:
                print(json.dumps({'error': 0,'table_data':multiOut}))
        else:
            INPUT = 3 # UPDATE
            query3 = """
                    select * from Persons 
                    """
            multiOut = executeQuery(query3)
            if (len(multiOut) == 0):
                print(json.dumps({'error': 1, 'message': "There was no data for your input: %s" % (opt)}))
            else:
                print(json.dumps({'error': 0,'table_data':multiOut}))

