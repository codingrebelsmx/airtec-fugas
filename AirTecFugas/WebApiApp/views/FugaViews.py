# -*- coding: utf-8 -*-
from ModelsApp.models import Fuga
from rest_framework import viewsets
from WebApiApp.serializers.FugaSerializers import FugaPointListSerializer

class FugaPointListView(viewsets.ModelViewSet):
    """description of class"""
    serializer_class = FugaPointListSerializer

    def get_queryset(self):
        id_empresa = self.request._request.session.get("id_cliente",None)
        id_planta = self.request._request.session.get("id_planta",None)
        if id_planta is None or id_empresa is None:
            return super().get_queryset()
        else:
            return Fuga.objects.filter(is_enabled=True, area__planta__id=id_planta).order_by('added')



