from django import forms
from django.core import validators

from user.models import user, examtest, UserTestModel


def name_check(value):
    if value.isalpha()!=True:
        raise forms.ValidationError("only string are allowed")



class userForm(forms.ModelForm):
    firstname = forms.CharField(widget=forms.TextInput(), required=True, max_length=100, validators=[name_check])
    lastname = forms.CharField(widget=forms.TextInput(), required=True, max_length=100, validators=[name_check])
    passwd = forms.CharField(widget=forms.PasswordInput(), required=True, max_length=100)
    email = forms.CharField(widget=forms.TextInput(), required=True)
    mobileno= forms.CharField(widget=forms.TextInput(), required=True, max_length=10,validators=[validators.MaxLengthValidator(10),validators.MinLengthValidator(10)])
    qualification = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    city = forms.CharField(widget=forms.TextInput(), required=True, max_length=100, validators=[name_check])
    status = forms.CharField(widget=forms.HiddenInput(), initial='waiting', max_length=100)
    def __str__(self):
        return self.email

    class Meta:
        model = user
        fields=['firstname','lastname','passwd','email','mobileno','qualification','city','status']


class examtestForm(forms.ModelForm):
    email = forms.CharField(widget=forms.TextInput(), required=True)
    question = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}), required=True, max_length=100)
    answer = forms.CharField(widget=forms.Textarea(), required=True, max_length=500)


    def __str__(self):
        return self.email

    class Meta:
        model=examtest
        fields=['email','question','answer']

class UserTestForm(forms.ModelForm):
    subject = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    email = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    question1 = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    answer1 = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    question2 = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    answer2 = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    question3 = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    answer3 = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    question4 = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    answer4 = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    question5 = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    answer5 = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    question6 = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    answer6 = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    question7 = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    answer7 = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    question8 = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    answer8 = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    question9 = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    answer9 = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    question10 = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    answer10 = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)

    def __str__(self):
        return self.subject

    class Meta:
        model=UserTestModel
        fields=['subject','email','question1','answer1','question2','answer2','question3','answer3','question4','answer4','question5','answer5','question6','answer6','question7','answer7','question8','answer9','question9','answer9','question10','answer10']


class MarksForm(forms.ModelForm):
    subject = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    email = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    marks = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)

    def __str__(self):
        return self.email

    class Meta:
        model=UserTestModel
        fields=['subject','email','marks']