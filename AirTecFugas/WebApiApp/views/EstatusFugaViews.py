# -*- coding: utf-8 -*-
from rest_framework.response import Response
from rest_framework import viewsets
from ModelsApp.models import Fuga
from WebApiApp.serializers.EstatusFugaSerializers import EstatusFugaSelectSerializer

class EstatusFugaListSelectView(viewsets.ModelViewSet):
    """ View to returns list of Ubicaciones with a form for Select Control """
    serializer_class = EstatusFugaSelectSerializer

    def get_queryset(self):
        return Fuga.estatus_fuga_dict
    
    def list(self, request, *args, **kwargs):
        estatus_fugas = Fuga.estatus_fuga_dict
        serializer = EstatusFugaSelectSerializer(instance=estatus_fugas, many=True)
        return Response(serializer.data)
