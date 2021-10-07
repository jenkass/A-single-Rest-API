from django.shortcuts import render
from .serializers import HeroSerializers
from rest_framework import viewsets
from .models import Hero
# Create your views here.


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializers