from django.urls import path
from .views import TeacherCreateView, LoginView, StudentCreateView

urlpatterns = [
    path('tc', TeacherCreateView.as_view(), name='teacher-create'),
    path('sc', StudentCreateView.as_view(), name='student-create'),
    path('l', LoginView.as_view(), name='login'),
]
