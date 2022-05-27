from connection import Connect
from pymongo import MongoClient

client =Connect.get_connection()

def insertTeacherData(username, firstname, lastname, email, password):
    # query to check if the database has a particular username
    query1 = client.teacher.users.count_documents({"username": username})
    # query to check if the database has a particular email
    query2 = client.teacher.users.count_documents({"email": email})

    # if both of them are zero then only proceed to enter into the db
    if query1 == 0 and query2 == 0: 
        client.teacher.users.insert_one({"username": username, "firstname": firstname, "lastname": lastname, "email": email, "password": password})
        print("Inserted")
        return True
    
    print("Teacher already Exists")
    return False

def insertStudentData(username, firstname, lastname, email, password):
    # query to check if the database has a particular username
    query1 = client.student.users.count_documents({"username": username})
    # query to check if the database has a particular username
    query2 = client.student.users.count_documents({"email": email})

    # if both of them are zero then only proceed to enter into the db
    if query1 == 0 and query2 == 0:
        client.student.users.insert_one({"username": username, "firstname": firstname, "lastname": lastname, "email": email, "password": password})
        print("Inserted")
        return True
    
    print("Student already Exists")
    return False

def signInAuthentication(username, email, password):
    # query to check if the database has a particular username
    query1 = client.teacher.users.count_documents({"username": username, "email": email, "password": password})
    # query to check if the database has a particular email
    query2 = client.student.users.count_documents({"username": username, "email": email, "password": password})
    if(query1==1):
        return 1
    elif(query2==1):
        return 2
    return 0

def getTeacherFname(username):
    return client.teacher.users.find_one({"username": username})['firstname']

def getTeacherLname(username):
    return client.teacher.users.find_one({"username": username})['lastname']

def getStudentFname(username):
    return client.student.users.find_one({"username": username})['firstname']

def getStudentLname(username):
    return client.student.users.find_one({"username": username})['lastname']

