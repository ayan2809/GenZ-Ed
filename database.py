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

def insertClassNumber(username, classnumber):
    if client.teacher.teacherCourses.count_documents({"username": username}) == 0:
        return client.teacher.teacherCourses.insert_one({"username": username, "classnumber": [classnumber]})
    else:
        return client.teacher.teacherCourses.update_one({"username": username}, {"$push": {"classnumber": classnumber}})

def getClassNumbers(username):
    return client.teacher.teacherCourses.find_one({"username": username})['classnumber']

def insertExtractedText(username,gradeNumber,
classNumber,courseName,moduleNumber,Extractedtext ):
    if client.materials.materialDetails.count_documents({"username": username, "gradeNumber": gradeNumber, "classNumber": classNumber, "courseName": courseName, "moduleNumber": moduleNumber}) == 0:
        return client.materials.materialDetails.insert_one({"username": username, "gradeNumber": gradeNumber, "classNumber": classNumber, "courseName": courseName, "moduleNumber": moduleNumber, "Extractedtext": [Extractedtext]})
        
    else:
        return client.materials.materialDetails.update_one({"username": username,"gradeNumber": gradeNumber, "classNumber": classNumber, "courseName": courseName, "moduleNumber": moduleNumber}, {"$push":{"Extractedtext": Extractedtext}})
    return True

def insertClassNumberStudent(username, classnumber):
    if client.student.studentCourses.count_documents({"username": username}) == 0:
        return client.student.studentCourses.insert_one({"username": username, "classnumber": [classnumber]})
    else:
        return client.student.studentCourses.update_one({"username": username}, {"$push": {"classnumber": classnumber}})

def getClassNumbersStudent(username):
    return client.student.studentCourses.find_one({"username": username})['classnumber']

def fetchUploadedMaterial( gradeNumber, classNumber, courseName, moduleNumber):
    return client.materials.materialDetails.find_one({"gradeNumber": gradeNumber, "classNumber": classNumber, "courseName": courseName, "moduleNumber": moduleNumber})


def insertQuestionData(username, gradeNumber, classNumber, courseName, moduleNumber, query, selected_text):
    if client.materials.questions.count_documents({"username": username, "gradeNumber": gradeNumber, "classNumber": classNumber, "courseName": courseName, "moduleNumber": moduleNumber}) == 0:
        return client.materials.questions.insert_one({"username": username, "gradeNumber": gradeNumber, "classNumber": classNumber, "courseName": courseName, "moduleNumber": moduleNumber, "questions": [{"question": query, "selected_text": selected_text}]})
    else:
        return client.materials.questions.update_one({"username": username,"gradeNumber": gradeNumber, "classNumber": classNumber, "courseName": courseName, "moduleNumber": moduleNumber}, {"$push":{"questions": {"question": query, "selected_text": selected_text}}})

def fetchQuestionsByStudents(gradeNumber, classNumber, courseName, moduleNumber):
    return client.materials.questions.find_one({"gradeNumber": gradeNumber, "classNumber": classNumber, "courseName": courseName, "moduleNumber": moduleNumber})

