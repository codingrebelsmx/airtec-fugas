# -*- coding: utf-8 -*-
from rest_framework import serializers


class RecomendacionFugaSelectSerializer(serializers.Serializer):

    id = serializers.CharField(max_length=3)
    nombre = serializers.CharField(max_length=100)

    class Meta:
        fields = ('id','nombre')

