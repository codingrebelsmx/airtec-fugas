# -*- coding: utf-8 -*-
from django.views.generic import DeleteView
from django.views.generic.detail import SingleObjectMixin
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.mixins import PermissionRequiredMixin
from MainApp.utils.SoftDeleterMixin import SoftDeleterMixin
from ModelsApp.models import Area
from ModelsApp.forms.AreaForms  import CreateAreaForm


class AreaDeleteView(PermissionRequiredMixin, SoftDeleterMixin, DeleteView):
    """  """
    """ Class to response a delete fuga request """
    model = Area
    form_class = CreateAreaForm
    template_name = 'MainApp/Area/delete-area.html'
    success_url = reverse_lazy('area-list')
    permission_required = ("ModelsApp.delete_area",)

