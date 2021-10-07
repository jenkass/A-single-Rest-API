from . import models
from rest_framework import serializers


class HeroSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Hero
        fields = ('name', 'alias')
