# -*- coding: utf-8 -*-
from ModelsApp.models import Fuga
from rest_framework import serializers


class FugaPointListSerializer(serializers.ModelSerializer):

    area = serializers.SlugRelatedField(many=False, read_only=True, slug_field='nombre')

    class Meta:
        model = Fuga
        fields = ('id','area', 'added', 'estatus', 'categoria', 'recomendacion', 'punto_x', 'punto_y')

