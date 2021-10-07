from django.shortcuts import render
from .serializers import HeroSerializers, LeadSerializer
from rest_framework import viewsets, generics
from .models import Hero, Lead
# Create your views here.


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializers


class LeadListCreate(generics.ListCreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer