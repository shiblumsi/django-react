from django.contrib import admin
from .models import Question,ChoiceOption
# Register your models here.

class QuestionModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'question']

class ChoiceOptionModelAdmin(admin.ModelAdmin):
    list_display = ['id','option', 'question']


admin.site.register(Question,QuestionModelAdmin)
admin.site.register(ChoiceOption,ChoiceOptionModelAdmin)

