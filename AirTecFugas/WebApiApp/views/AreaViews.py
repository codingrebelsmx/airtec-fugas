# -*- coding: utf-8 -*-
from ModelsApp.models import Area
from rest_framework import viewsets
from WebApiApp.serializers.AreaSerializers import AreaSelectSerializer

class AreaListSelectView(viewsets.ModelViewSet):
    """ View to returns list of Ubicaciones with a form for Select Control """
    serializer_class = AreaSelectSerializer
    queryset = Area.objects.filter(is_enabled=True)
   
