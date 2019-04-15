# -*- coding: utf-8 -*-
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import CreateView
from django.urls import reverse_lazy
from ModelsApp.models import Empresa
from ModelsApp.forms.EmpresaForms import CreateEmpresaForm


class CreateEmpresaPartialView(PermissionRequiredMixin, CreateView):
    """ View to respond for a request to create a new empresa """

    model = Empresa
    form_class = CreateEmpresaForm
    template_name = "MainApp/Empresa/create-empresa-partial.html"
    success_url = reverse_lazy('empresa-list')
    permission_required = ("ModelsApp.add_empresa",)


