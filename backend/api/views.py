from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView

from .models import Car, Person
from .serializers import PersonSerializer, PersonListSerializer, PersonUpdateSerializer, CreateCarSerializer, ListCarSerializer


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


class CreateCarView(CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CreateCarSerializer

class CarListView(ListAPIView):
    queryset = Car.objects.all()
    serializer_class = ListCarSerializer

