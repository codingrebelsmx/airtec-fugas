# -*- coding: utf-8 -*-
from ModelsApp.models import Area
from rest_framework import viewsets
from WebApiApp.serializers.AreaSerializers import AreaSelectSerializer

class AreaListSelectView(viewsets.ModelViewSet):
    """ View to returns list of Ubicaciones with a form for Select Control """
    serializer_class = AreaSelectSerializer
    queryset = Area.objects.filter(is_enabled=True)


    def get_queryset(self):
        id_empresa = self.request._request.session.get("id_cliente",None)
        id_planta = self.request._request.session.get("id_planta",None)
        if id_planta is None or id_empresa is None:
            return super().get_queryset()
        else:
            return Area.objects.filter(is_enabled=True, planta__id=id_planta).order_by('nombre')
   
