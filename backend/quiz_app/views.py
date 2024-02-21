from django.shortcuts import render
from rest_framework.generics import CreateAPIView,ListAPIView

from .models import Question
from .serializers import QuestionSerializer, QuestionSerializerList

# Create your views here.
class QuestionView(CreateAPIView):
    questions = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionViewList(ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
