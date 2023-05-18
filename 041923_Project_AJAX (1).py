#!/usr/bin/env python3

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
  if (query == "singlePatientSearch"):
    pt_id = form.getvalue("id","") 
    pt_id = pt_id.strip()
    singleQuery = """
    select * from Persons where PersonID = %s
    """
    singleOut = executeQuery(singleQuery, [pt_id])
    if (len(singleOut) == 0):
      print(json.dumps({'error': 1, 'message': "There was no data for the patient id %s" % (pt_id)}))
    else:
      print(json.dumps({'error': 0,'table_data':singleOut}))
