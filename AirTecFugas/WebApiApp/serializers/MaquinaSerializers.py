# -*- coding: utf-8 -*-
from ModelsApp.models import Maquina
from rest_framework import serializers


class MaquinaSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maquina
        fields = ('id','nombre')

