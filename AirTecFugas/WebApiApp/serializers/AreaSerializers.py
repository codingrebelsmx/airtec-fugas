# -*- coding: utf-8 -*-
from ModelsApp.models import Area
from rest_framework import serializers


class AreaSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ('id','nombre')
