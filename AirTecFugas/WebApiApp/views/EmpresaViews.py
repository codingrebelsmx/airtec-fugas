# -*- coding: utf-8 -*-
from ModelsApp.models import Empresa
from rest_framework import viewsets
from WebApiApp.serializers.EmpresaSerializers import EmpresaSelectSerializer

class EmpresaListSelectView(viewsets.ModelViewSet):
    """ View to returns list of Ubicaciones with a form for Select Control """
    serializer_class = EmpresaSelectSerializer
    queryset = Empresa.objects.filter(is_enabled=True)
   

