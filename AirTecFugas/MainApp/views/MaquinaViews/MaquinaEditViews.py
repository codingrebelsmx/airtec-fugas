# -*- coding: utf-8 -*-
from django.views.generic import UpdateView, DetailView
from django.views.generic.detail import SingleObjectMixin
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.mixins import PermissionRequiredMixin
from ModelsApp.models import Maquina
from ModelsApp.forms.MaquinaForms import CreateMaquinaForm


class MaquinaEditView(PermissionRequiredMixin, UpdateView):
    """  """
    model = Maquina
    form_class = CreateMaquinaForm
    template_name = "MainApp/Maquina/update-maquina.html"
    success_url = reverse_lazy('maquina-list')
    permission_required = ("ModelsApp.change_maquina",)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        area_seleccionada = "MAQUINAS"
        context["menu"] = area_seleccionada
        return context




class MaquinaPartialEditView(PermissionRequiredMixin, UpdateView):
    """  """
    model = Maquina
    form_class = CreateMaquinaForm
    template_name = "MainApp/Maquina/update-partial-maquina.html"
    success_url = reverse_lazy('maquina-list')
    permission_required = ("ModelsApp.change_maquina",)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        id_empresa = self.request.session.get("id_cliente",None)
        id_planta = self.request.session.get("id_planta",None)
        if id_planta is not None and id_empresa is not None:
            context["id_cliente"] = id_empresa
            context["id_planta"] = id_planta
        else:
            context["id_cliente"] = self.request.user.empresa.id
        return context
