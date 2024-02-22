from rest_framework import serializers

from .models import Car, Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['name', 'email', 'phone_number', 'date_of_birth', 'gender', 'is_married', 'address', 'photo']


class PersonListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

class PersonUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['name', 'email', 'phone_number', 'date_of_birth', 'gender', 'is_married', 'address', 'photo']

class CreateCarSerializer(serializers.ModelSerializer):
    person = serializers.PrimaryKeyRelatedField(queryset=Person.objects.all())
    class Meta:
        model = Car
        fields = ['title', 'model_name', 'brand', 'person']
    depth = 1

    def create(self, validated_data):
        print(validated_data)
        return Car.objects.create(**validated_data)


class ListCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'
        depth = 1
