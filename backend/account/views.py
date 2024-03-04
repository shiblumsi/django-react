from rest_framework.generics import CreateAPIView
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser
from .serializers import TeacherRegisterSerializer, LoginSerializer, StudentRegisterSerializer


class TeacherCreateView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = TeacherRegisterSerializer

class StudentCreateView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = StudentRegisterSerializer
class LoginView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = LoginSerializer

    def perform_create(self, serializer):
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
        return serializer
