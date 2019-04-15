# -*- coding: utf-8 -*-
from django.views.generic import DeleteView
from django.views.generic.detail import SingleObjectMixin
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.mixins import PermissionRequiredMixin
from MainApp.utils.SoftDeleterMixin import SoftDeleterMixin
from ModelsApp.models import Maquina
from ModelsApp.forms.MaquinaForms  import CreateMaquinaForm


class MaquinaDeleteView(PermissionRequiredMixin, SoftDeleterMixin, DeleteView):
    """ Class to response a delete maquina request """
    model = Maquina
    form_class = CreateMaquinaForm
    template_name = 'MainApp/Maquina/delete-maquina.html'
    success_url = reverse_lazy('maquina-list')
    permission_required = ("ModelsApp.delete_maquina",)


