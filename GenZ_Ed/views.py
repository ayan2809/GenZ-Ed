from pdb import post_mortem
from tkinter import E
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

def index(request):
    return render(request, 'index.html')

def authentication(request):
    return render(request, 'login_signup.html')

# def teacherprofile(request):
#     return render(request, 'teacherprofile.html')

# def studentprofile(request):
#     return render(request, 'studentprofile.html')

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
                return render(request, template_name='teacherprofile.html', context={'username': username})
        else:
            status= insertStudentData(username, fname, lname, email, pass1)

            if status==False:
                return redirect('/failure')
            else:
                return render(request, template_name='studentprofile.html', context={'username': username})
        
        
        
    return render(request, "activate.html")

def activate(request):
    return render(request, 'activate.html')

def profile(request):
    if request.method == "POST":
        username= request.POST.get("signInUsername")
        email = request.POST.get("signInEmail")
        password= request.POST.get("signInPassword")
        print(username,email,password)
        if(username=="" or email=="" or password==""):
            return redirect('/failure')
        else:
            status= signInAuthentication(username, email, password)
            if status==0:
                return redirect('/failure')
            elif status==1:
                return render(request, template_name='teacherprofile.html', context={'username': username})
                # return redirect('/teacherprofile?username='+username)
            elif status==2:
                return render(request, template_name='studentprofile.html', context={'username': username})
                # return redirect('/studentprofile?username='+username)

    # return render(request, 'activate.html')