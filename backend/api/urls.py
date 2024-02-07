from django.urls import path
from .views import PersonCreateView, PersonListView


urlpatterns = [
    path('pc', PersonCreateView.as_view(), name='person-create'),
    path('pl/', PersonListView.as_view(), name='person-list'),
]