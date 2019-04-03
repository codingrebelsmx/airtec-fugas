# -*- coding: utf-8 -*-
from django.views.generic import DeleteView
from django.views.generic.detail import SingleObjectMixin
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.mixins import PermissionRequiredMixin
from MainApp.utils.SoftDeleterMixin import SoftDeleterMixin
from ModelsApp.models import Fuga
from ModelsApp.forms.FugaForms  import CreateFugaForm


class FugaDeleteView(PermissionRequiredMixin, SoftDeleterMixin, DeleteView):
    """ Class to response a delete fuga request """
    model = Fuga
    form_class = CreateFugaForm
    template_name = 'MainApp/Fuga/delete-fuga.html'
    success_url = reverse_lazy('fuga-list')
    permission_required = ("ModelsApp.delete_fuga",)

    



