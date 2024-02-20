from django.contrib import admin
from .models import Question, ChoiceOption, AnswerQuestion


# Register your models here.

class QuestionModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'question']


class ChoiceOptionModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'option', 'question']


class AnswerQuestionModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'answer', 'question']


admin.site.register(Question, QuestionModelAdmin)
admin.site.register(ChoiceOption, ChoiceOptionModelAdmin)
admin.site.register(AnswerQuestion, AnswerQuestionModelAdmin)
