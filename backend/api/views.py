from rest_framework.generics import CreateAPIView, ListAPIView

from .models import Person
from .serializers import PersonSerializer, PersonListSerializer


class PersonCreateView(CreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonListView(ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonListSerializer


