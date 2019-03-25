# -*- coding: utf-8 -*-
from rest_framework import serializers


class EstatusFugaSelectSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    nombre = serializers.CharField(max_length=100)

    class Meta:
        fields = ('id','nombre')

