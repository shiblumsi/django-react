from django.urls import path

from .views import UserRegistrationView, UserLoginView, UserLogoutView

urlpatterns = [
    path('ur/', UserRegistrationView.as_view(), name='user-registration'),
    path('ul/', UserLoginView.as_view(), name='user-login'),
    path('lo/', UserLogoutView.as_view(), name='user-logout'),

]
