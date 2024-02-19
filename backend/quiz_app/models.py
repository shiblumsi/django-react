from django.db import models


# Create your models here.
class Question(models.Model):
    question = models.CharField(max_length=255)



class ChoiceOption(models.Model):
    option = models.CharField(max_length=255)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
