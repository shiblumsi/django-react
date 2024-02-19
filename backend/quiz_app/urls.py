from django.urls import path
from .views import QuestionView

urlpatterns = [
    path('qc', QuestionView.as_view(), name='question-create')
]
