    # -*- coding: utf-8 -*-
from django.views.generic import CreateView
from django.urls import reverse_lazy
from ModelsApp.models import Area
from ModelsApp.forms.AreaForms import CreateAreaPartialForm


class AreaCreatePartialView(CreateView):
    """description of class"""

    model = Area
    form_class = CreateAreaPartialForm
    template_name = "MainApp/Area/create-area-partial.html"
    success_url = reverse_lazy('area-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id_planta = self.request.session.get("id_planta", None)
        if id_planta is not None:
            context["id_planta"] = id_planta
        return context

    def get_object(self, queryset=None):
        object = super().get_object(queryset)
        object.id_planta = self.request.session.get("id_planta", None)
        return object
