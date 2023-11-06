from django.shortcuts import render
from rest_framework import generics 
from .serializer import HomeMiddleSerializer 
from main.models import Furniture 

# Create your views here.

class FurnitureList(generics.ListAPIView): 

    serializer_class = HomeMiddleSerializer 

    def get_queryset(self): 

        user = self.request.user 

        return Furniture.objects.all()
