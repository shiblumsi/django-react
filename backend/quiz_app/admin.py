from django.contrib import admin
from .models import Question, ChoiceOption, AnswerQuestion, ResultQuiz


# Register your models here.

class QuestionModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'question']


class ChoiceOptionModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'option', 'question']


class AnswerQuestionModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'answer', 'question']

class ResultQuizModelAdmin(admin.ModelAdmin):
    list_display = ['question', 'is_currect']


admin.site.register(Question, QuestionModelAdmin)
admin.site.register(ChoiceOption, ChoiceOptionModelAdmin)
admin.site.register(AnswerQuestion, AnswerQuestionModelAdmin)
admin.site.register(ResultQuiz, ResultQuizModelAdmin)
