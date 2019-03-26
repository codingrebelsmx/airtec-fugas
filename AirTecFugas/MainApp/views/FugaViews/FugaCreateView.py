# -*- coding: utf-8 -*-
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from ModelsApp.models import Fuga
from ModelsApp.forms.FugaForms import CreateFugaForm


class FugaCreateView(CreateView):
    """ View to register a new Fuga """
    model = Fuga
    form_class = CreateFugaForm
    template_name = "MainApp/Fuga/create-fuga.html"
    success_url = reverse_lazy('fuga-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id_tecnico = self.request.user.id
        context["id_tecnico"] = id_tecnico
        return context

    def dispatch(self, request, *args, **kwargs):
        cliente = self.request.session.get("id_cliente", None)
        planta = self.request.session.get("id_planta", None)

        if cliente != None and planta != None:
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect('selec-planta-trabajo')


    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.tecnico = self.request.user.id
        return obj

