from django.urls import path
from .views import QuestionView,QuestionViewList,ResultQuizView

urlpatterns = [
    path('qc/', QuestionView.as_view(), name='question-create'),
    path('ql/', QuestionViewList.as_view(), name='question-list'),
    path('qr/', ResultQuizView.as_view(), name='question-result-create'),
]
