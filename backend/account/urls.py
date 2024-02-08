from django.urls import path
from .views import UserRegistrationView,UserRegistrationView2

urlpatterns = [
    path('ur', UserRegistrationView.as_view(), name='user-registration'),
    path('ur2', UserRegistrationView2.as_view(), name='user-registration'),
]