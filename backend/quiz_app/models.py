from django.db import models


# Create your models here.
class Question(models.Model):
    question = models.CharField(max_length=255)

    def __str__(self):
        return self.question


class ChoiceOption(models.Model):
    option = models.CharField(max_length=255)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')

    def __str__(self):
        return self.option


class AnswerQuestion(models.Model):
    answer = models.CharField(max_length=255)
    question = models.OneToOneField(Question, on_delete=models.CASCADE, related_name='answer_question')

    def __str__(self):
        return self.answer


class ResultQuiz(models.Model):
    user = models.CharField(max_length=1)
    question = models.ForeignKey(Question, on_delete=models.CASCADE,related_name='result_quizzes')
    selected_option = models.ForeignKey(ChoiceOption, on_delete=models.CASCADE)
    is_currect = models.BooleanField(default=False)
