# -*- coding: utf-8 -*-
from rest_framework.response import Response
from rest_framework import viewsets
from ModelsApp.models import Fuga
from WebApiApp.serializers.RecomendacionFugaSerializers import RecomendacionFugaSelectSerializer

class RecomendacionFugaListSelectView(viewsets.ModelViewSet):
    """ View to returns list of Ubicaciones with a form for Select Control """
    serializer_class = RecomendacionFugaSelectSerializer

    def get_queryset(self):
        return Fuga.estatus_fuga_dict
    
    def list(self, request, *args, **kwargs):
        recomendacion_fugas = Fuga.recomendaciones_dict
        serializer = RecomendacionFugaSelectSerializer(instance=recomendacion_fugas, many=True)
        return Response(serializer.data)

