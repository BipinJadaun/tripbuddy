from django.shortcuts import render
from rest_framework import generics
from .models import User
from .serializers import UserSerializer

# Create your views here.

class UserListView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()