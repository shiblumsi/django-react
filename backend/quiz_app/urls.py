from django.urls import path
from .views import QuestionView,QuestionViewList

urlpatterns = [
    path('qc/', QuestionView.as_view(), name='question-create'),
    path('ql/', QuestionViewList.as_view(), name='question-list'),
]
