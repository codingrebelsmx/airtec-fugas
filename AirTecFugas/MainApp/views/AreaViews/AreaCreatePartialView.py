    # -*- coding: utf-8 -*-
from django.views.generic import CreateView
from django.urls import reverse_lazy
from ModelsApp.models import Area
from ModelsApp.forms.AreaForms import CreateAreaForm


class AreaCreatePartialView(CreateView):
    """description of class"""

    model = Area
    form_class = CreateAreaForm
    template_name = "MainApp/Area/create-area-partial.html"
    success_url = reverse_lazy('area-list')


