from ModelsApp.models import Maquina
from rest_framework import viewsets
from WebApiApp.serializers.MaquinaSerializers import MaquinaSelectSerializer

class MaquinaListSelectView(viewsets.ModelViewSet):
    """ View to returns list of Ubicaciones with a form for Select Control """
    serializer_class = MaquinaSelectSerializer
    
    def get_queryset(self):
        id_area = self.kwargs.get('id_area',None)
        queryset = Maquina.objects.filter(is_enabled=True, area__id=id_area) if id_area is not None else Maquina.objects.filter(is_enabled=True)
        return queryset
