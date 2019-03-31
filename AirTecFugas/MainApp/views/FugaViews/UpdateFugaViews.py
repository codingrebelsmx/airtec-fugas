# -*- coding: utf-8 -*-
from django.views.generic import UpdateView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.mixins import PermissionRequiredMixin
from ModelsApp.models import Fuga, ImagenFuga
from ModelsApp.forms.FugaForms import CreateFugaForm


class FugaCorregidaUpdateView(PermissionRequiredMixin, UpdateView):
    """ View to register a new Fuga """
    model = Fuga
    template_name = "MainApp/Fuga/create-fuga.html"
    success_url = reverse_lazy('fuga-list')
    permission_required = ("ModelsApp.change_fuga",)
