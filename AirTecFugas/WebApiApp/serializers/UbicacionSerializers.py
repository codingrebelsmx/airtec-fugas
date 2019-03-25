# -*- coding: utf-8 -*-
from ModelsApp.models import Ubicacion
from rest_framework import serializers


class UbicacionSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ubicacion
        fields = ('id','nombre')

