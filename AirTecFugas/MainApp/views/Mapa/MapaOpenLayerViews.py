from django.views.generic import TemplateView


class MapaFugasOpenLayerView(TemplateView):
    """ View experimental para desplegar mapas con open layers """
    template_name = "MainApp/Mapa/mapa-fugas.html"



