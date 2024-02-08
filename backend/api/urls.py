from django.urls import path
from .views import PersonCreateView, PersonListView, PersonUpdateView, PersonDeleteView


urlpatterns = [
    path('pc/', PersonCreateView.as_view(), name='person-create'),
    path('pl/', PersonListView.as_view(), name='person-list'),
    path('pu/<int:pk>/', PersonUpdateView.as_view(), name='person-update'),
    path('pd/<int:pk>/', PersonDeleteView.as_view(), name='person-delete'),
]