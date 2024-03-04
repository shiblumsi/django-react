# from rest_framework import serializers
#
#
# class UserRegistrationSerializer(serializers.Serializer):
#     username = serializers.CharField(max_length=255)
#     email = serializers.EmailField(max_length=255)
#     password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
#     password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
#
#     def create(self, validated_data):
#         password = validated_data.pop('password')
#         password2 = validated_data.pop('password2')
#         if password != password2:
#             raise serializers.ValidationError("Password not matched!")
#         return User.objects.create(password=password, **validated_data)
#
#
# class UserLoginSerializer(serializers.Serializer):
#     username = serializers.CharField(max_length=255)
#     password = serializers.CharField()

from rest_framework import serializers
from .models import CustomUser


class TeacherRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'password2']

    def create(self, validated_data):
        password = validated_data.pop('password')
        password2 = validated_data.pop('password2')
        if password != password2:
            raise serializers.ValidationError("Password not matched!")
        return CustomUser.objects.create_teacher(password=password, **validated_data)


class StudentRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'password2']

    def create(self, validated_data):
        password = validated_data.pop('password')
        password2 = validated_data.pop('password2')
        if password != password2:
            raise serializers.ValidationError("Password not matched!")
        return CustomUser.objects.create_student(password=password, **validated_data)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
