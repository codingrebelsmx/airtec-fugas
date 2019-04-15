# -*- coding: utf-8 -*-
from django.views.generic import CreateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from ModelsApp.models import Maquina
from ModelsApp.forms.MaquinaForms import CreateMaquinaForm

class MaquinaCreatePartialView(PermissionRequiredMixin, CreateView):
    """description of class"""

    model = Maquina
    form_class = CreateMaquinaForm
    template_name = "MainApp/Maquina/create-maquina-partial.html"
    success_url = reverse_lazy('maquina-list')
    permission_required = ("ModelsApp.add_maquina",)
