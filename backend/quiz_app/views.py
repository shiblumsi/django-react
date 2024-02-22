from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView

from .models import Question, ResultQuiz
from .serializers import QuestionSerializer, ResultSerializer


# Create your views here.
class QuestionView(CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionViewList(ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class ResultQuizView(CreateAPIView):
    queryset = ResultQuiz.objects.all()
    serializer_class = ResultSerializer

    def perform_create(self, serializer):
        print(serializer.data)
        return serializer
