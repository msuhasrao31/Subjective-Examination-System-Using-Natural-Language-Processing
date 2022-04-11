from django.contrib import admin

from examination.models import questionsModel,ExaminationQuestionModel
# Register your models here.

admin.site.register(questionsModel)
admin.site.register(ExaminationQuestionModel)
