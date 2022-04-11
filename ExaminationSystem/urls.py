"""ExaminationSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from user import views as user
from examination import views as examination
from ExaminationSystem import views as ExaminationSystem



urlpatterns = [
    path('admin/', admin.site.urls),
    #path('hello/', teacher.hello),
    path('index/', user.index, name='index'),
    path('userpage/', user.userpage, name='userpage'),
    path('userlogin/', user.userlogin, name='userlogin'),
    path('userregister/', user.userregister, name='userregister'),
    path('userlogincheck/', user.userlogincheck, name='userlogincheck'),
    path('usertest/', user.usertest, name='usertest'),
    path('examtest/', user.examtest, name='examtest'),
    path('usertestcheck/', user.usertestcheck, name='usertestcheck'),
    path('usersanswers/', user.usersanswers, name='usersanswers'),
    path('finalmarks/', user.finalmarks, name='finalmarks'),


    path('examinationlogin/', examination.examinationlogin, name='examinationlogin'),
    path('examinationregister/', examination.examinationregister, name='examinationregister'),
    path('examinationcheck/', examination.examinationcheck, name='examinationcheck'),
    path('usersdata/', examination.usersdata, name='usersdata'),
    path('questioncell/', examination.questioncell, name='questioncell'),
    path('examquestions/', examination.examquestions, name='examquestions'),
    path('qanswers/', examination.qanswers, name='qanswers'),
    path('userresult/', examination.userresult, name='userresult'),
    path('examresult/', examination.examresult, name='examresult'),



    path('adminlogin/', ExaminationSystem.adminlogin, name='adminlogin'),
    path('adminloginentered/', ExaminationSystem.adminloginentered, name='adminloginentered'),
    path('viewuserdata/', ExaminationSystem.viewuserdata, name='viewuserdata'),
    path('examinationquestionsdata/', ExaminationSystem.examinationquestionsdata, name='examinationquestionsdata'),
    path('examinationanswersdata/', ExaminationSystem.examinationanswersdata, name='examinationanswersdata'),
    path('userstestdata/', ExaminationSystem.userstestdata, name='userstestdata'),
    path('activateuser/', ExaminationSystem.activateuser, name='activateuser'),
    path('examinationuserdata/', ExaminationSystem.examinationuserdata, name='examinationuserdata'),
    path('activateexamination/', ExaminationSystem.activateexamination, name='activateexamination'),
    path('logout/', ExaminationSystem.logout, name='logout'),




]
