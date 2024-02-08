from django.shortcuts import render
from .serializers import UserRegistrationSerializer, ReS
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView


# Create your views here.

class UserRegistrationView(APIView):

    def get(self, request):
        users = User.objects.all()
        serializer = UserRegistrationSerializer(users, many=True)
        return Response({"users": serializer.data})

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Success": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"Error": serializer.data}, status=status.HTTP_400_BAD_REQUEST)


class UserRegistrationView2(CreateAPIView):
    serializer_class = ReS
    queryset = User.objects.all()
