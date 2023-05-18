#!/usr/bin/env python3

import pymysql
import cgi
import cgitb
import json

cgitb.enable()

form = cgi.FieldStorage()

print("Content-type: text/html\n")


queryGenderCount = """
Select count(*) from `_D2DEMO` group by PERSON_GENDER;
"""

queryEthnicityCount = """
Select count(*) from `_D2DEMO` group by ETHN_GRP_CAT_TXT;
"""

queryRaceCount = """
Select count(*) from `_D2DEMO` group by RACE_CAT_TXT;
"""

queryEducationCount = """
Select count(*) from _D2PCDEMO Group by PT_COMPL_SCHOOL;
"""

queryAgeCount = """
Select AGE from _D2ELIGCHECK;
"""

question1a = """
Select count(*) from _D2ELIGCHECK where PT_HX_COPD_EMP_YN like "yes";
"""
question1b = """
Select newID from _D2ELIGCHECK where PT_HX_COPD_EMP_YN like "yes";
"""

question2a = """
Select count(*) from _D2ELIGCHECK where GRPB_SMK_STS like "Former Smoker";
"""

question2b = """
Select D2ELIGCHECKID from _D2ELIGCHECK where GRPB_SMK_STS like "Former Smoker";
"""

question3a = """
Select count(distinct newID) from _D2PHYEXAM where BLD_PRESS_SYSTOLIC >= 140 and BLD_PRESS_DIASTOLIC >= 90;
"""

question3b = """
Select distinct newID from _D2PHYEXAM where BLD_PRESS_SYSTOLIC >= 140 and BLD_PRESS_DIASTOLIC >= 90;
"""

question4a = """
Select count(*) from _D2ELIGCHECK where GRPB_SMK_STS = "Current Smoker";
"""

question4b = """
Select D2ELIGCHECKID from _D2ELIGCHECK where GRPB_SMK_STS = "Current Smoker";
"""

question5a = """
Select count(*) from _D2PCSYMPCBE where PT_COMPL_SBRTH_YN like "Yes";
"""

question5b = """
Select D2PCSYMPCBEID from _D2PCSYMPCBE where PT_COMPL_SBRTH_YN like "Yes";
"""

singlePatientQuery = """
Select newID, ETHN_GRP_CAT_TXT, PERSON_GENDER, PT_COMPL_SMOK_STAT, PT_COMPL_SMOK_HAB, PT_COMPL_CIG_DAY from _D2DEMO JOIN _D2PCSMKHX using(newID) where newID = %s
"""

multiPatientQuery = "Select newID, ETHN_GRP_CAT_TXT, PERSON_GENDER, PT_COMPL_SMOK_STAT, PT_COMPL_SMOK_HAB, PT_COMPL_CIG_DAY from _D2DEMO JOIN _D2PCSMKHX using(newID) where newID IN (%s, 3)"

listPatientQuery = "Select newID, ETHN_GRP_CAT_TXT, PERSON_GENDER, PT_COMPL_SMOK_STAT, PT_COMPL_SMOK_HAB, PT_COMPL_CIG_DAY from _D2DEMO JOIN _D2PCSMKHX using(newID) where newID IN (%s, 3, 4, 5, 6, 7)"



try:
    connection = pymysql.connect(
        host='bioed.bu.edu', 
        user='isarfraz',
        password='isarfraz', 
        db='Team_G',
        port = 4253) 
except pymysql.Error as e: 
    print(e)

cursor = connection.cursor()

if form:
    selector = form.getvalue("selector", "")
    id = form.getvalue("id", "")
    if(selector == "genderCount"):
        try: 
            cursor.execute(queryGenderCount)
        except pymysql.Error as e: 
            print(e,queryGenderCount)
        
        results = cursor.fetchall()
        print(json.dumps(results))
    elif(selector == "ethnicityCount"):
        try: 
            cursor.execute(queryEthnicityCount)
        except pymysql.Error as e: 
            print(e,queryEthnicityCount)
        
        results = cursor.fetchall()
        print(json.dumps(results)) 
    elif(selector == "ageCount"):
        try: 
            cursor.execute(queryAgeCount)
        except pymysql.Error as e: 
            print(e,queryAgeCount)
        
        results = cursor.fetchall()
        print(json.dumps(results)) 
    elif(selector == "raceCount"):
        try: 
            cursor.execute(queryRaceCount)
        except pymysql.Error as e: 
            print(e,queryRaceCount)
        
        results = cursor.fetchall()
        print(json.dumps(results))
    elif(selector == "educationCount"):
        try: 
            cursor.execute(queryEducationCount)
        except pymysql.Error as e: 
            print(e,queryEducationCount)
        
        results = cursor.fetchall()
        print(json.dumps(results))
    elif(selector == "q1a"):
        try: 
            cursor.execute(question1a)
        except pymysql.Error as e: 
            print(e,question1a)
        
        results = cursor.fetchall()
        print(json.dumps(results))
    elif(selector == "q1b"):
        try: 
            cursor.execute(question1b)
        except pymysql.Error as e: 
            print(e,question1b)
        
        results = cursor.fetchall()
        print(json.dumps(results))
    elif(selector == "q2a"):
        try: 
            cursor.execute(question2a)
        except pymysql.Error as e: 
            print(e,question2a)
        results = cursor.fetchall()
        print(json.dumps(results))
    
    elif(selector == "q2b"):
        try: 
            cursor.execute(question2b)
        except pymysql.Error as e: 
            print(e,question2b)
        
        results = cursor.fetchall()
        print(json.dumps(results))
    elif(selector == "q3a"):
        try: 
            cursor.execute(question3a)
        except pymysql.Error as e: 
            print(e,question3a)
        results = cursor.fetchall()
        print(json.dumps(results))
    
    elif(selector == "q3b"):
        try: 
            cursor.execute(question3b)
        except pymysql.Error as e: 
            print(e,question3b)
        
        results = cursor.fetchall()
        print(json.dumps(results))
    elif(selector == "q4a"):
        try: 
            cursor.execute(question4a)
        except pymysql.Error as e: 
            print(e,question4a)
        results = cursor.fetchall()
        print(json.dumps(results))
    
    elif(selector == "q4b"):
        try: 
            cursor.execute(question4b)
        except pymysql.Error as e: 
            print(e,question4b)
        
        results = cursor.fetchall()
        print(json.dumps(results))
    elif(selector == "q5a"):
        try: 
            cursor.execute(question5a)
        except pymysql.Error as e: 
            print(e,question5a)
        results = cursor.fetchall()
        print(json.dumps(results))
    
    elif(selector == "q5b"):
        try: 
            cursor.execute(question5b)
        except pymysql.Error as e: 
            print(e,question5b)
        
        results = cursor.fetchall()
        print(json.dumps(results))
    elif(selector == "wholePatientSearch"):
        findColumnQuery = "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE COLUMN_NAME = %s;"
        cursor.execute(findColumnQuery, [id])
        table_name = cursor.fetchone()[0]
        fullAttributeQuery = "Select {} from {};".format(','.join(["newID", id]), table_name)
        try: 
            cursor.execute(fullAttributeQuery)
        except pymysql.Error as e: 
            print(e,fullAttributeQuery)
        
        results = cursor.fetchall()
        print(json.dumps(results))
else:
    print("Content-type: text/html\n")