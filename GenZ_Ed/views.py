from select import select
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from GenZ_Ed import settings
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth import authenticate, login, logout
from . tokens import generate_token
from database import *

from rest_framework.decorators import api_view
from rest_framework.response import Response
import os
import openai

import environ
env = environ.Env()
environ.Env.read_env()

openai.api_key=env('OPENAI_API_KEY')


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
            'List': '/GetClassNumbers',
            # 'Detail View' : '/task-detail/<str:pk>/',
            'Create1' : '/UpdateClassNumber/',
            # 'Update' : '/task-update/<str:pk>/',
            # 'Delete' : '/task-delete/<str:pk>/',
        }
    return Response(api_urls)

def index(request):
    return render(request, 'index.html')

def authentication(request):
    return render(request, 'login_signup.html')

def failure(request):
    return render(request, 'failure.html')
def signup(request):
    if request.method == "POST":
        print("signup")
        print(request)
        username = request.POST.get("uname")
        fname= request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        position = request.POST.get("position")
        pass1 = request.POST.get("pass1")
        pass2 = request.POST.get("pass2")
        print(username,fname,lname,email,position,pass1,pass2)
        if(position=='Teacher' or position=='teacher'):
            status= insertTeacherData(username, fname, lname, email, pass1)
            if status==False:
                return redirect('/failure')
            else:
                return render(request, template_name='teacherprofile.html', context={'username': username,'email':email, 'name':fname+" "+lname})
        else:
            status= insertStudentData(username, fname, lname, email, pass1)

            if status==False:
                return redirect('/failure')
            else:
                return render(request, template_name='studentprofile.html', context={'username': username,'email':email, 'name':fname+" "+lname})
        
        
        
    return render(request, "activate.html")

def activate(request):
    return render(request, 'activate.html')

def profile(request):
    if request.method == "POST":
        username= request.POST.get("signInUsername")
        email = request.POST.get("signInEmail")
        password= request.POST.get("signInPassword")
        # print(username,email,password)
        if(username=="" or email=="" or password==""):
            return redirect('/failure')
        else:
            status= signInAuthentication(username, email, password)
            if status==0:
                return redirect('/failure')
            elif status==1:
                fname= getTeacherFname(username)
                lname= getTeacherLname(username)
                return render(request, template_name='teacherprofile.html', context={'username': username,'email':email, 'name':fname+" "+lname})
                
            elif status==2:
                fname= getStudentFname(username)
                lname= getStudentLname(username)
                return render(request, template_name='studentprofile.html', context={'username': username,'email':email, 'name':fname+" "+lname})
                

    return render(request, 'profile.html')


@api_view(['POST'])
def UpdateClassNumber(request):
    username= request.data['username']
    classNumber= request.data['classNumber']
    insertClassNumber(username, classNumber)
    # print(response)
    # print(request.data)
    # if response==True:
    return Response({"message":"success"})
    # else:
    #     return Response({"message":"failure"})

@api_view(['POST'])
def GetClassNumbers(request):
    # print(request.data)
    data=getClassNumbers(request.data['username'])
    return Response({ 'status': 'Fetched', 'data':data})

@api_view(['POST'])
def UploadExtractedText(request):
    username= request.data['username']
    gradeNumber = request.data['gradeNumber']
    classNumber = request.data['classNumber']
    courseName = request.data['courseName']
    moduleNumber = request.data['moduleNumber']
    Extractedtext= request.data['Extractedtext']
    # print(username,gradeNumber,classNumber,courseName,moduleNumber,Extractedtext)
    insertExtractedText(username, gradeNumber, classNumber, courseName, moduleNumber, Extractedtext)
    return Response({"message":"success"})

@api_view(['POST'])
def UpdateClassNumberStudent(request):
    username= request.data['username']
    classNumber= request.data['classNumber']
    insertClassNumberStudent(username, classNumber)
    return Response({"message":"success"})

@api_view(['POST'])
def GetClassNumbersStudent(request):
    print(request.data)
    data=getClassNumbersStudent(request.data['username'])
    return Response({ 'status': 'Fetched', 'data':data})

@api_view(['POST'])
def FetchUploadedMaterial(request):
    # print(request.data)
    data=fetchUploadedMaterial(request.data['gradeNumber'],request.data['classNumber'],request.data['courseName'],request.data['moduleNumber'])

    data= data['Extractedtext']

    return Response({ 'status': 'Fetched', 'data':data})

@api_view(['POST'])
def GetSummary(request):
    data=request.data['text']
    # print(openai.api_key)
    # print(data)
    response = openai.Completion.create(
    engine="text-davinci-002",
    prompt="Summarize this for a second-grade student:"+data,
    temperature=0.7,
    max_tokens=100,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
    )
    # print(response)
    return Response({"message":response['choices'][0]['text']})

@api_view(['POST'])
def chatBotReply(request):
    data=request.data['text']
    query=request.data['query']
    username= request.data['username']
    gradeNumber = request.data['gradeNumber']
    classNumber = request.data['classNumber']
    courseName = request.data['courseName']
    moduleNumber = request.data['moduleNumber']
    # print(data, query)
    response = openai.Answer.create(
    search_model="ada",
    model="curie",
    question=query,
    documents=[ data],
    examples_context="World War 2",
    examples=[["When did the german invasion happen?","It happened in 1939"]],
    max_tokens=50,
    stop=["\n", "<|endoftext|>"],
    )
    selected_text= response['selected_documents'][0]
    selected_text =selected_text['text']
    insertQuestionData(username, gradeNumber, classNumber, courseName, moduleNumber, query, selected_text)
    # documents=[data],
    # query="When did the german invasion happen?"
    # )
    # print(openai.api_key)
    # print(data)
    # response = openai.Completion.create(
    # engine="davinci-custom",
    # prompt="What is your name?",
    # temperature=0.7,
    # max_tokens=100,
    # top_p=1.0,
    # frequency_penalty=0.0,
    # presence_penalty=0.0
    # )
    # print(response)
    return Response({
    "status":200,"message":"success",
    "answers":response['answers'][0]})




# openai.api_key = os.getenv("OPENAI_API_KEY")
# @api_view(['POST'])
# def GetSummary(request):
    
    # response = openai.Completion.create(
    # engine="text-davinci-002",
    # prompt="Summarize this for a second-grade student:\n\nJupiter is the fifth planet from the Sun and the largest in the Solar System. It is a gas giant with a mass one-thousandth that of the Sun, but two-and-a-half times that of all the other planets in the Solar System combined. Jupiter is one of the brightest objects visible to the naked eye in the night sky, and has been known to ancient civilizations since before recorded history. It is named after the Roman god Jupiter.[19] When viewed from Earth, Jupiter can be bright enough for its reflected light to cast visible shadows,[20] and is on average the third-brightest natural object in the night sky after the Moon and Venus.",
    # temperature=0.7,
    # max_tokens=64,
    # top_p=1.0,
    # frequency_penalty=0.0,
    # presence_penalty=0.0
    # )
    # return Response({"message":"success"})

