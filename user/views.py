from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse

from examination.models import questionsModel, ExaminationQuestionModel
from user.forms import *
from user.models import user, MarksModel


def index(request):
    return render(request,'index.html')

def userpage(request):
    return render(request,'user/userpage.html')

def userlogin(request):
    return render(request,"user/userlogin.html")

def userregister(request):
    if request.method=='POST':
        form1=userForm(request.POST)
        if form1.is_valid():
            form1.save()
            return render(request, "user/userlogin.html")
            #return HttpResponse("registreration succesfully completed")
        else:
            print("form not valied")
            return HttpResponse("form not valied")
    else:
        form=userForm()
        return render(request,"user/userregister.html",{"form":form})

def userlogincheck(request):
    if request.method == "POST":
        email = request.POST.get('uname')
        pswd = request.POST.get('upasswd')
        print("Email = ", email, ' Password = ', pswd)
        try:
            check = user.objects.get(email=email,passwd=pswd)
            status = check.status
            print('Status is = ', status)
            if status == "Activated":
                request.session['id'] = check.id
                #request.session['name'] = check.name
                request.session['email'] = check.email
                print("User id At", check.id, status,check.email)
                return render(request, 'user/userpage.html', {})
            else:
                messages.success(request, 'Your Account Not at activated')
                return render(request, 'user/userlogin.html')
            # return render(request, 'user/userpage.html',{})
        except Exception as e:
            print('Exception is ', str(e))
            pass
        messages.success(request, 'Invalid Email id and password')
    return render(request, 'user/userlogin.html')

def usertest(request):
    return render(request,"user/subject.html")

def usertestcheck(request):
    if request.method == "POST":
        subject = request.POST.get('subject')

        print("subject = ", subject)

        check = ExaminationQuestionModel.objects.get(subject=subject)
        print("check",check)
        print(check.question1)
        return render(request, 'user/userquestions.html', {"object":check})



def examtest(request):
    if request.method=='POST':
        email = request.POST.get('email')
        #question = request.POST.get('question')
        #answer = request.POST.get('answer')
        questions = request.POST.getlist('qtn[]')
        answers = [request.POST['answer-{}'.format(q)] for q in questions]
        print("Kattama code ",questions,'==',answers)
        questions = request.POST.getlist('answers')
        print("question",type(questions),questions)
        answers = [request.POST['answer-{}'.format(q)] for q in questions]
        print("email",email,"question",questions,"answer",answers)
        form1 = examtestForm(request.POST)
        if form1.is_valid():
            form1.save()
            return render(request, "user/userpage.html")
            #return HttpResponse("registreration succesfully completed")
        else:
            print("form not valied")
            return HttpResponse("form not valied")
    else:
        form = examtestForm()
        return render(request,"user/usertest.html",{"object":form})

def usersanswers(request):
    if request.method=='POST':
        email = request.session['email']
        subject = request.POST.get('subject')
        question1 = request.POST.get('question1')
        answer1 = request.POST.get('answer1')
        question2 = request.POST.get('question2')
        answer2 = request.POST.get('answer2')
        question3 = request.POST.get('question3')
        answer3 = request.POST.get('answer3')
        question4 = request.POST.get('question4')
        answer4 = request.POST.get('answer4')
        question5 = request.POST.get('question5')
        answer5 = request.POST.get('answer5')
        question6 = request.POST.get('question6')
        answer6 = request.POST.get('answer6')
        question7 = request.POST.get('question7')
        answer7 = request.POST.get('answer7')
        question8 = request.POST.get('question8')
        answer8 = request.POST.get('answer8')
        question9 = request.POST.get('question9')
        answer9 = request.POST.get('answer9')
        question10 = request.POST.get('question10')
        answer10 = request.POST.get('answer10')
        print(email,subject,question1,answer1,question2,answer2,question3,answer3,question4,answer4,question5,answer5,question6,answer6,question7,answer7,question8,answer8,question9,answer9,question10,answer10,)
        UserTestModel.objects.create(email=email,subject=subject,question1=question1,answer1=answer1,question2=question2,answer2=answer2,question3=question3,answer3=answer3,
                                     question4=question4,answer4=answer4,question5=question5,answer5=answer5,question6=question6,answer6=answer6,question7=question7,
                                     answer7=answer7,question8=question8,answer8=answer8,question9=question9,answer9=answer9,question10=question10,answer10=answer10)
        print("succesfully saved the data")
        return render(request,'user/answerstore.html')



def finalmarks(request):
    email = request.session['email']
    object = MarksModel.objects.filter(email=email)
    return render(request,"user/userresult.html",{"marks":object})