from . import models
from rest_framework import serializers


class HeroSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Hero
        fields = ('name', 'alias')


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Lead
        fields = ('id', 'name', 'email', 'message')