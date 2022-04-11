from django.db import models

# Create your models here.
class examination(models.Model):
    firstname = models.CharField(max_length=50,default="", editable=True)
    lastname = models.CharField(max_length=50,default="", editable=True)
    email = models.EmailField()
    passwd = models.CharField(max_length=40)
    mobileno = models.CharField(max_length=50, default="", editable=True)
    qualification = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    status = models.CharField(max_length=40,default="", editable=True)

    def __str__(self):
        return self.email
    class Meta:
        db_table='examinationregister'

class ExaminationQuestionModel(models.Model):
    subject = models.CharField(max_length=50, default="", editable=True, unique=True)
    question1 = models.CharField(max_length=500, default="", editable=True)
    question2 = models.CharField(max_length=500, default="", editable=True)
    question3 = models.CharField(max_length=500, default="", editable=True)
    question4 = models.CharField(max_length=500, default="", editable=True)
    question5 = models.CharField(max_length=500, default="", editable=True)
    question6 = models.CharField(max_length=500, default="", editable=True)
    question7 = models.CharField(max_length=500, default="", editable=True)
    question8 = models.CharField(max_length=500, default="", editable=True)
    question9 = models.CharField(max_length=500, default="", editable=True)
    question10 = models.CharField(max_length=500, default="", editable=True)

    def __str__(self):
        return self.subject
    class Meta:
        db_table="ExaminationQuestionTable"


class ExaminationAnswerModel(models.Model):
    subject = models.CharField(max_length=50, default="", editable=True, unique=True)
    answer1 = models.CharField(max_length=500, default="", editable=True)
    answer2 = models.CharField(max_length=500, default="", editable=True)
    answer3 = models.CharField(max_length=500, default="", editable=True)
    answer4 = models.CharField(max_length=500, default="", editable=True)
    answer5 = models.CharField(max_length=500, default="", editable=True)
    answer6 = models.CharField(max_length=500, default="", editable=True)
    answer7 = models.CharField(max_length=500, default="", editable=True)
    answer8 = models.CharField(max_length=500, default="", editable=True)
    answer9 = models.CharField(max_length=500, default="", editable=True)
    answer10 = models.CharField(max_length=500, default="", editable=True)

    def __str__(self):
        return self.subject
    class Meta:
        db_table="ExaminationAnswerTable"


class questionsModel(models.Model):
    subject = models.CharField(max_length=50, default="", editable=True, unique=True)
    question1 = models.CharField(max_length=500, default="", editable=True)
    question2 = models.CharField(max_length=500, default="", editable=True)
    question3 = models.CharField(max_length=500, default="", editable=True)
    question4 = models.CharField(max_length=500, default="", editable=True)
    question5 = models.CharField(max_length=500, default="", editable=True)
    question6 = models.CharField(max_length=500, default="", editable=True)
    question7 = models.CharField(max_length=500, default="", editable=True)
    question8 = models.CharField(max_length=500, default="", editable=True)
    question9 = models.CharField(max_length=500, default="", editable=True)
    question10 = models.CharField(max_length=500, default="", editable=True)
    def __str__(self):
        return self.id
    class Meta:
        db_table="questionstable"
