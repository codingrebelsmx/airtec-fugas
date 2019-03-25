    # -*- coding: utf-8 -*-
from django.views.generic import CreateView
from django.urls import reverse_lazy
from ModelsApp.models import Planta
from ModelsApp.forms.PlantaForms import CreatePlantaForm


class CreatePlantaPartialView(CreateView):
    """description of class"""

    model = Planta
    form_class = CreatePlantaForm
    template_name = "MainApp/Planta/create-planta-partial.html"
    success_url = reverse_lazy('planta-list')


