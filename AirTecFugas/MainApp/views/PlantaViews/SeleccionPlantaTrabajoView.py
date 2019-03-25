# -*- coding: utf-8 -*-
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from ModelsApp.forms.AreaTrabajoForms import SeleccionPlantaTrabajoForm



class SeleccionPlantaTrabajoView(FormView):
    """ View to select planta de trabajo """
    template_name = "MainApp/PlantaTrabajo/seleccion-planta-trabajo.html"
    form_class = SeleccionPlantaTrabajoForm
    success_url = reverse_lazy("dashboard")

    def get(self, request, *args, **kwargs):
        cliente = self.request.session.get("id_cliente", None)
        planta = self.request.session.get("id_planta", None)

        if cliente != None and planta != None:
            return redirect("dashboard")
        return super().get(request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


    def form_valid(self, form):
        self.request.session.pop("id_cliente", form.cleaned_data['cliente'])
        self.request.session.pop("id_planta", form.cleaned_data['planta'])
        return super().form_valid(form)


