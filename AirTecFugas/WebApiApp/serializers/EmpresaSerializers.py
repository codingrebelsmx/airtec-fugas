# -*- coding: utf-8 -*-
from ModelsApp.models import Empresa
from rest_framework import serializers


class EmpresaSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = ('id','nombre')

