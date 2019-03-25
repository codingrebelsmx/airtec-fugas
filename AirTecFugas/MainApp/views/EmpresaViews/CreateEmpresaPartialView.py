    # -*- coding: utf-8 -*-
from django.views.generic import CreateView
from django.urls import reverse_lazy
from ModelsApp.models import Empresa
from ModelsApp.forms.EmpresaForms import CreateEmpresaForm


class CreateEmpresaPartialView(CreateView):
    """description of class"""

    model = Empresa
    form_class = CreateEmpresaForm
    template_name = "MainApp/Empresa/create-empresa-partial.html"
    success_url = reverse_lazy('empresa-list')


