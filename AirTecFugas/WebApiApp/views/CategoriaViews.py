# -*- coding: utf-8 -*-
from rest_framework.response import Response
from rest_framework import viewsets
from ModelsApp.models import Fuga
from WebApiApp.serializers.CategoriaFugaSerializers import CategoriaSelectSerializer

class CategoriaListSelectView(viewsets.ModelViewSet):
    """ View to returns list of Ubicaciones with a form for Select Control """
    serializer_class = CategoriaSelectSerializer

    def get_queryset(self):
        return Fuga.categorias_dict
    
    def list(self, request, *args, **kwargs):
        categorias = Fuga.categorias_dict
        serializer = CategoriaSelectSerializer(instance=categorias, many=True)
        return Response(serializer.data)

