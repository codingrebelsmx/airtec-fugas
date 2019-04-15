    # -*- coding: utf-8 -*-
from django.views.generic import CreateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from ModelsApp.models import Planta
from ModelsApp.forms.PlantaForms import CreatePlantaForm


class CreatePlantaPartialView(PermissionRequiredMixin, CreateView):
    """description of class"""

    model = Planta
    form_class = CreatePlantaForm
    template_name = "MainApp/Planta/create-planta-partial.html"
    success_url = reverse_lazy('planta-list')
    permission_required = ("ModelsApp.add_planta",)

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
