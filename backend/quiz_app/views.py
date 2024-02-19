from django.shortcuts import render
from rest_framework.generics import CreateAPIView

from .models import Question
from .serializers import QuestionSerializer

# Create your views here.
class QuestionView(CreateAPIView):
    questions = Question.objects.all()
    serializer_class = QuestionSerializer