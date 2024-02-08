from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView

from .models import Person
from .serializers import PersonSerializer, PersonListSerializer, PersonUpdateSerializer


class PersonCreateView(CreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonListView(ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonListSerializer

class PersonUpdateView(UpdateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonUpdateSerializer

class PersonDeleteView(DestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

