from django.shortcuts import render
from rest_framework import generics
from .serializers import PlaceSerializer
from .models import Place

# Create your views here.

class PlaceListView(generics.ListCreateAPIView):
    serializer_class = PlaceSerializer
    queryset = Place.objects.all()

class PlaceDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PlaceSerializer
    queryset = Place.objects.all()