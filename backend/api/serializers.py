from rest_framework import serializers

from .models import Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['name', 'email', 'phone_number', 'date_of_birth', 'gender', 'is_married', 'address', 'photo']


class PersonListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'
