from rest_framework import serializers
from django.contrib.auth.models import User


class UserRegistrationSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField()
    password2 = serializers.CharField()

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')

        if password and password2 and password != password2:
            raise serializers.ValidationError("Password do not match")
        return attrs

    def create(self, validated_data):
        password2 = validated_data.pop('password2')  # Remove password2 before creating the user
        user = User.objects.create_user(**validated_data)
        return user


class ReS(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
