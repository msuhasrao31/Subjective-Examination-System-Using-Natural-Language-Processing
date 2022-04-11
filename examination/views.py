from django.contrib import messages
from django.shortcuts import render
import nltk
# Create your views here.
from examination.forms import examinationForm,  examinationanswerForm, examinationquestionForm
from django.http import HttpResponse

from examination.models import *
from user.models import *


def examinationlogin(request):
    return render(request,"examination/examinationlogin.html")

def examinationregister(request):
    if request.method=='POST':
        form1=examinationForm(request.POST)
        if form1.is_valid():
            form1.save()
            return render(request, "examination/examinationlogin.html")
            #return HttpResponse("registreration succesfully completed")
        else:
            print("form not valied")
            return HttpResponse("form not valied")
    else:
        form=examinationForm()
        return render(request,"examination/examinationregister.html",{"form":form})


def examinationcheck(request):
    if request.method == "POST":
        email = request.POST.get('uname')
        pswd = request.POST.get('upasswd')
        print("Email = ", email, ' Password = ', pswd)
        try:
            check = examination.objects.get(email=email,passwd=pswd)
            status = check.status
            print('Status is = ', status)
            if status == "Activated":
                request.session['id'] = check.id
                #request.session['name'] = check.name
                request.session['email'] = check.email
                print("User id At", check.id, status)
                return render(request, 'examination/examinationpage.html', {})
            else:
                messages.success(request, 'Your Account Not at activated')
                return render(request, 'examination/examinationlogin.html')
            # return render(request, 'user/userpage.html',{})
        except Exception as e:
            print('Exception is ', str(e))
            pass
        messages.success(request, 'Invalid Email id and password')
    return render(request, 'examination/examinationlogin.html')

def usersdata(request):
    object = user.objects.all()
    return render(request,"examination/userdata.html",{"object":object})


"""def examcell(request):
    if request.method == 'POST':
        form1=ExaminationQuestionForm(request.POST)
        subject = request.POST.get('subject')
        question1 = request.POST.get('question1')
        question2 = request.POST.get('question2')
        question3 = request.POST.get('question3')
        question4 = request.POST.get('question4')
        question5 = request.POST.get('question5')
        question6 = request.POST.get('question6')
        question7 = request.POST.get('question7')
        question8 = request.POST.get('question8')
        question9 = request.POST.get('question9')
        question10 = request.POST.get('question10')
        print("subject",subject,"question1",question1,"question2",question2,"question3",question3,"question4",question4,"question5",question5,"question6",question6,"question7",question7,"question8",question8,"question9",question9,"question10",question10)
        if form1.is_valid():
            form1.save()
            return render(request, "examination/success.html")
            #return HttpResponse("registreration succesfully completed")
        else:
            print("form not valied")
            return HttpResponse("form not valied")
    else:
        form = ExaminationQuestionForm()
        return render(request,"examination/examcell.html",{"form":form})"""

def questioncell(request):
    if request.method=='POST':
        form1=examinationquestionForm(request.POST)
        if form1.is_valid():
            form1.save()
            return render(request, "examination/success.html")
            #return HttpResponse("registreration succesfully completed")
        else:
            print("form not valied")
            return HttpResponse("form not valied")
    else:
        form=examinationquestionForm()
        return render(request,"examination/examcell.html",{"form":form})

def examquestions(request):
    if request.method=='POST':
        form1=examinationquestionForm(request.POST)
        if form1.is_valid():
            form1.save()
            return render(request, "examination/success.html")
            #return HttpResponse("registreration succesfully completed")
        else:
            print("form not valied")
            return HttpResponse("form not valied")
    else:
        form=examinationquestionForm()
        return render(request,"examination/examquestions.html",{"form":form})

def qanswers(request):
    if request.method=='POST':
        form1=examinationanswerForm(request.POST)
        if form1.is_valid():
            form1.save()
            return render(request, "examination/answersuccess.html")
            #return HttpResponse("registreration succesfully completed")
        else:
            print("form not valied")
            return HttpResponse("form not valied")
    else:
        form=examinationanswerForm()
        return render(request,"examination/examanswers.html",{"form":form})

def userresult(request):
    object = UserTestModel.objects.all()
    return render(request, "examination/examdata.html", {"object": object})

def examresult(request):
    if request.method=='GET':
        subject = request.GET.get('subject')
        email = request.GET.get('email')
        print("email",email)
        object = ExaminationAnswerModel.objects.get(subject=subject)
        print("object", object.answer1,object.answer2)
        s=''
        s=s+object.answer1+" "+object.answer2+" "+object.answer3+" "+object.answer4+" "+object.answer5+" "+object.answer6+" "+object.answer7+" "+object.answer8+" "+object.answer9+" "+object.answer10
        print("answers",s)
        words = s.split()
        remove = ' '.join(sorted(set(words), key=words.index))
        print("remove duplicate words",remove)
        p = ''.join(e for e in remove if e.isalnum())
        print("remove punctivations",p)
        object1 = UserTestModel.objects.get(email=email)
        print("object1",object1.answer1)
        s1 = ''
        s1 = s1+object1.answer1+" "+object1.answer2+" "+object1.answer3+" "+object1.answer4+" "+object1.answer5+" "+object1.answer6+" "+object1.answer7+" "+object1.answer8+" "+object1.answer9+" "+object1.answer10
        print("student answers",s1)
        words = s1.split()
        nltk = ' '.join(sorted(set(words), key=words.index))
        print("remove duplicate words", nltk)
        p1 = ''.join(e for e in nltk if e.isalnum())
        print("remove punctivations for users", p1)
        m = len(p)+len(p1)
        count,i=0 ,0
        for x in p1:
            if x == p[i]:
                count=count+1
                print(count)
                i=i+1
            else:
                i=i+1
        print("count:",count)
        print("p1-len:",len(p1))
        if count == len(p1):
            marks = (count/len(p1))*100
        elif count <= len(p1):
            marks = (count/len(p1))*100


        result = MarksModel.objects.create(subject=subject,email=email,marks=marks)
        result.save()
        return render(request, "examination/examinationpage.html",{'marks':marks})