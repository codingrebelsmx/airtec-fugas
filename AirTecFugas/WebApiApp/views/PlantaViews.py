# -*- coding: utf-8 -*-
from ModelsApp.models import Planta
from rest_framework import viewsets
from WebApiApp.serializers.PlantaSerializers import PlantaSelectSerializer

class PlantaListSelectView(viewsets.ModelViewSet):
    """ View to returns list of Ubicaciones with a form for Select Control """
    serializer_class = PlantaSelectSerializer
    
    def get_queryset(self):
        id_empresa = self.kwargs.get('id_empresa',None)
        queryset = Planta.objects.filter(is_enabled=True, empresa__id=id_empresa).order_by('nombre') if id_empresa is not None else Planta.objects.filter(is_enabled=True).order_by('pk')
        return queryset


