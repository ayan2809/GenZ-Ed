"""GenZ_Ed URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
# from django.conf.urls import re_path
from django.views.static import serve
from django.conf import settings
from django.urls import include

urlpatterns = [
    # path('',views.apiOverview, name = "api-overview"),
    path('admin/', admin.site.urls),
    path('', views.index, name = 'index'),
    path('authentication/', views.authentication, name = 'authentication'),
    path('GetClassNumbers', views.GetClassNumbers, name = 'GetClassNumbers'),
    path('UpdateClassNumber', views.UpdateClassNumber, name = 'UpdateClassNumber'),
    path('signup', views.signup, name='signup'),
    path('profile', views.profile, name='profile'),
    # path('teacherprofile', views.teacherprofile, name='teacherprofile'),
    # path('studentprofile', views.studentprofile, name='studentprofile'),
    path('logout', views.logout, name='logout'),
    path('failure', views.failure, name='failure'),
    
    path('UpdateClassNumber/',views.UpdateClassNumber, name = "UpdateClassNumber"),
    path('GetClassNumbers/',views.GetClassNumbers, name = "GetClassNumbers"),
    path('UploadExtractedText/',views.UploadExtractedText, name = "UploadExtractedText"),
    # path('', include("Home.urls")),

      path(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]

