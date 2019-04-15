# -*- coding: utf-8 -*-
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from ModelsApp.forms.AreaTrabajoForms import SeleccionPlantaTrabajoForm



class SeleccionPlantaTrabajoView(LoginRequiredMixin, FormView):
    """ View to select planta de trabajo """
    template_name = "MainApp/PlantaTrabajo/seleccion-planta-trabajo.html"
    form_class = SeleccionPlantaTrabajoForm
    success_url = reverse_lazy("dashboard")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        area_seleccionada = "TRABAJO"
        context["menu"] = area_seleccionada
        context["ejecutivo"] = self.request.user.groups.all().filter(name="Ejecutivos").first() != None
        context["id_empresa"] = self.request.user.empresa.id if context["ejecutivo"] else None
        return context

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except Exception as excep:
            return "Error"

    def form_valid(self, form):
        self.request.session["id_cliente"] = form.cleaned_data['cliente']
        self.request.session["id_planta"] = form.cleaned_data['planta']
        return super().form_valid(form)


