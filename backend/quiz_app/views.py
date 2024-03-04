from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView

from .models import Question, ResultQuiz, AnswerQuestion, ChoiceOption
from .serializers import QuestionSerializer, ResultQuizSerializer2, ResultSerializer, ResultQuizSerializer


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
        question_and_options = serializer.validated_data['question_options']
        for q_id, o_id in question_and_options.items():
            q=Question.objects.get(id=q_id)
            qa = AnswerQuestion.objects.get(question__id=q_id)
            qo = ChoiceOption.objects.get(id=o_id)
            print(qa.answer, qo.option)
            if(qa.answer==qo.option):
                ResultQuiz.objects.create(selected_option=qo,question=q,is_currect=True)
            else:
                ResultQuiz.objects.create(selected_option=qo, question=q)
        return serializer


class ResultQuizViewList(ListAPIView):
    queryset = Question.objects.all()
    serializer_class = ResultQuizSerializer2