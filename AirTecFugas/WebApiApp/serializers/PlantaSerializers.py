# -*- coding: utf-8 -*-
from ModelsApp.models import Planta
from rest_framework import serializers


class PlantaSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planta
        fields = ('id','nombre')

