    # -*- coding: utf-8 -*-
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse, HttpResponseForbidden, Http404
from django.urls import reverse_lazy
from ModelsApp.models import Planta
from ModelsApp.forms.PlantaForms import CreatePlantaForm


class PlanoPlantaView(LoginRequiredMixin, DetailView):
    """ View que permitirá retornar el contenido del archivo svg del plano de la planta """
    model = Planta
    template_name = ""


    def get_object(self, queryset=None):
        id_planta = self.request.session.get("id_planta", None)

        if id_planta == None:
            return super().get_object(queryset)
        else:
            return Planta.objects.filter(pk=id_planta, is_enabled=True).first()


    def render_to_response(self, context, **response_kwargs):
        if self.object is not None and self.object.plano is not None:
            return HttpResponse(self.object.plano.file, content_type="image/svg+xml")
        else:
            return Http404("La planta no tiene un plano asignado")

