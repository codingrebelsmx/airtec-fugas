# -*- coding: utf-8 -*-
from django.views.generic import UpdateView, DetailView
from django.views.generic.detail import SingleObjectMixin
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.mixins import PermissionRequiredMixin
from ModelsApp.models import Fuga, ImagenFuga
from ModelsApp.forms.FugaForms import CreateFugaForm


class FugaEditView(PermissionRequiredMixin, UpdateView):
    """  """
    model = Fuga
    form_class = CreateFugaForm
    template_name = "MainApp/Fuga/update-fuga.html"
    success_url = reverse_lazy('fuga-list')
    permission_required = ("ModelsApp.change_fuga",)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        area_seleccionada = "FUGAS"
        context["menu"] = area_seleccionada
        return context


class FugaEditLayoutPointView(PermissionRequiredMixin, UpdateView):
    """  """
    model = Fuga
    form_class = CreateFugaForm
    template_name = "MainApp/Fuga/mapa-fugas-edit.html"
    success_url = reverse_lazy('fuga-list')
    permission_required = ("ModelsApp.change_fuga",)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        area_seleccionada = "FUGAS"
        context["menu"] = area_seleccionada
        return context



class FugaPartialEditView(PermissionRequiredMixin, UpdateView):
    """  """
    model = Fuga
    form_class = CreateFugaForm
    template_name = "MainApp/Fuga/update-partial-fuga.html"
    success_url = reverse_lazy('fuga-list')
    permission_required = ("ModelsApp.change_fuga",)



class FugaCorregidaEditView(PermissionRequiredMixin, DetailView):
    """  """
    model = Fuga
    template_name = "MainApp/Fuga/update-corregir-fuga.html"
    permission_required = ("ModelsApp.change_fuga",)
    queryset = Fuga.objects.filter(is_enabled=True)


    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super().get_object(queryset)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        nuevo_estado = next(filter(lambda x: x["nombre"].upper() == "CORREGIDO", Fuga.estatus_fuga_dict), None)
        if self.object is not None and nuevo_estado is not None:
            self.object.estatus = nuevo_estado.get("id", None)
            self.object.save()
            return HttpResponse(content="Ok")
        else:
            raise Http404()




