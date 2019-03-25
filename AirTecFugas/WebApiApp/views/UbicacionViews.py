# -*- coding: utf-8 -*-
from ModelsApp.models import Ubicacion
from rest_framework import viewsets
from WebApiApp.serializers.UbicacionSerializers import UbicacionSelectSerializer

class UbicacionListSelectView(viewsets.ModelViewSet):
    """ View to returns list of Ubicaciones with a form for Select Control """
    serializer_class = UbicacionSelectSerializer
    queryset = Ubicacion.objects.filter(is_enabled=True)

