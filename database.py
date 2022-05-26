from connection import Connect
from pymongo import MongoClient

client =Connect.get_connection()

def insertTeacherData(username, firstname, lastname, email, password):
    cursor = client.teacher.users.count_documents({"username": username})
    # print(cursor)
    if cursor == 0:
        client.teacher.users.insert_one({"username": username, "firstname": firstname, "lastname": lastname, "email": email, "password": password})
        print("Inserted")
        return True
    
    print("Teacher already Exists")
    return False

def insertStudentData(username, firstname, lastname, email, password):
    cursor = client.student.users.count_documents({"username": username})
    if cursor == 0:
        client.student.users.insert_one({"username": username, "firstname": firstname, "lastname": lastname, "email": email, "password": password})
        print("Inserted")
        return True
    
    print("Student already Exists")
    return False