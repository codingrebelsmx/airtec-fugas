# -*- coding: utf-8 -*-
from django.views.generic import CreateView
from django.urls import reverse_lazy
from ModelsApp.models import Area
from django.contrib.auth.mixins import PermissionRequiredMixin
from ModelsApp.forms.AreaForms import CreateAreaForm


class AreaCreateView(PermissionRequiredMixin, CreateView):
    """description of class"""

    model = Area
    form_class = CreateAreaForm
    template_name = "MainApp/Area/create-area.html"
    success_url = reverse_lazy('area-list')
    permission_required = ("ModelsApp.add_area",)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        area_seleccionada = "AREAS"
        context["menu"] = area_seleccionada
        return context
        


