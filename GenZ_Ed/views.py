from pdb import post_mortem
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

def profile(request):
    return render(request, 'profile.html')

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
                return redirect('/profile')
        else:
            status= insertStudentData(username, fname, lname, email, pass1)

            if status==False:
                return redirect('/failure')
            else:
                return redirect('/profile')
        
        
        
    return render(request, "activate.html")

def activate(request):
    return render(request, 'activate.html')

def signin(request):
    return render(request, 'activate.html')