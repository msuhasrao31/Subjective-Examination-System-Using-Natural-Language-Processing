from django.shortcuts import render
from django.http import HttpResponse

from examination.models import examination, ExaminationQuestionModel, ExaminationAnswerModel
from user.models import user, UserTestModel


def adminlogin(request):
    return render(request, "admin/adminlogin.html")

def adminloginentered(request):
    if request.method == 'POST':
        uname=request.POST['uname']
        passwd=request.POST['upasswd']
        if uname == 'admin' and passwd == 'admin':
            return render(request,"admin/adminloginentered.html")
        else:
            return HttpResponse("invalied credentials")


def logout(request):
    return render(request,'index.html')

def viewuserdata(request):
    object = user.objects.all()
    return render(request,"admin/viewuserdata.html",{"object":object})

def activateuser(request):
    if request.method =='GET':
        uname=request.GET.get('pid')
        print(uname)
        status='Activated'
        print("pid=",uname,"status=",status)
        user.objects.filter(id=uname).update(status=status)
        object=user.objects.all()
        return render(request,"admin/viewuserdata.html",{"object":object})

def examinationuserdata(request):
    object = examination.objects.all()
    return render(request,"admin/examinationuserdata.html",{"object":object})

def activateexamination(request):
    if request.method =='GET':
        uname=request.GET.get('pid')
        print(uname)
        status='Activated'
        print("pid=",uname,"status=",status)
        examination.objects.filter(id=uname).update(status=status)
        object=examination.objects.all()
        return render(request,"admin/examinationuserdata.html",{"object":object})

def examinationquestionsdata(request):
    object = ExaminationQuestionModel.objects.all()
    return render(request,"admin/examinationquestionsdata.html",{"object":object})

def examinationanswersdata(request):
    object = ExaminationAnswerModel.objects.all()
    return render(request,"admin/examinationanswersdata.html",{"object":object})

def userstestdata(request):
    object = UserTestModel.objects.all()
    return render(request,"admin/userstestdata.html",{"object":object})
    