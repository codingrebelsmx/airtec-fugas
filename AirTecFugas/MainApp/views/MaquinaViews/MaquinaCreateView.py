# -*- coding: utf-8 -*-
from django.views.generic import CreateView
from django.urls import reverse_lazy
from ModelsApp.models import Maquina
from ModelsApp.forms.MaquinaForms import CreateMaquinaForm

class MaquinaCreateView(CreateView):
    """description of class"""

    model = Maquina
    form_class = CreateMaquinaForm
    template_name = "MainApp/Maquina/create-maquina.html"
    success_url = reverse_lazy('maquina-list')
