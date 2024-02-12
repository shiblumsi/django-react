from django.contrib.auth import authenticate, login, logout
from .serializers import UserRegistrationSerializer, UserLoginSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView


class UserRegistrationView(CreateAPIView):
    serializer_class = UserRegistrationSerializer
    queryset = User.objects.all()


class UserLoginView(APIView):
    def post(self, request, format=None):
        username = request.data.get('username')
        password = request.data.get('password')
        print(username,password,request,request.data)
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return Response({"detail": "Login successful."}, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)
    # def post(self, request):
    #     serializer = UserLoginSerializer(data=request.data)
    #     if serializer.is_valid():
    #         print(serializer.data.get('username'), serializer.data.get('password'))
    #         user = authenticate(request, username=serializer.data.get('username'), password=serializer.data.get('password'))
    #         print('true' if user else 'false')
    #         if user is not None:
    #             login(request, user)
    #             return Response({"status": "Login Success"}, status=status.HTTP_200_OK)
    #     return Response({"status": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class UserLogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({"detail": "Logged out successfully."}, status=status.HTTP_200_OK)
