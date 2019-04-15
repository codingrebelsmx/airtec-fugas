# -*- coding: utf-8 -*-
from django.views.generic import ListView
from ModelsApp.models import Area
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.mixins import PermissionRequiredMixin


class AreaListView(PermissionRequiredMixin, ListView):
    """ Abstract class to response for list of fugas request """
    model = Area
    template_name = "MainApp/Area/list-area.html"
    permission_required = ("ModelsApp.view_area",)


    def dispatch(self, request, *args, **kwargs):
        cliente = self.request.session.get("id_cliente", None)
        planta = self.request.session.get("id_planta", None)

        if cliente != None and planta != None:
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect('selec-planta-trabajo')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        area_seleccionada = "AREAS"
        context["menu"] = area_seleccionada

        id_empresa = self.request.session.get("id_cliente",None)
        id_planta = self.request.session.get("id_planta",0)
        if id_planta is not None and id_empresa is not None:
            context["id_cliente"] = id_empresa
            context["id_planta"] = id_planta
        else:
            context["id_cliente"] = self.request.user.empresa.id

        return context
    

    def get_queryset(self):
        id_planta = self.request.session.get("id_planta", None)

        if id_planta == None:
            return super().get_queryset(queryset)
        else:
            return Area.objects.filter(planta__id=id_planta, is_enabled=True).order_by("-updated")



