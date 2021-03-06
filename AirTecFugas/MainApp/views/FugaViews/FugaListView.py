# -*- coding: utf-8 -*-
from django.views.generic import ListView
from django.http import HttpResponse, Http404
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.mixins import PermissionRequiredMixin
from ModelsApp.models import Fuga
import csv


class FugaListView(PermissionRequiredMixin, ListView):
    """ Abstract class to response for list of fugas request """
    model = Fuga
    template_name = "MainApp/Fuga/list-fuga.html"
    permission_required = ("ModelsApp.view_fuga",)


    def dispatch(self, request, *args, **kwargs):
        cliente = self.request.session.get("id_cliente", None)
        planta = self.request.session.get("id_planta", None)

        if cliente != None and planta != None:
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect('selec-planta-trabajo')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        area_seleccionada = "FUGAS"
        context["menu"] = area_seleccionada
        return context
    

    def get_queryset(self):
        id_planta = self.request.session.get("id_planta", None)

        if id_planta == None:
            return super().get_queryset(queryset)
        else:
            return Fuga.objects.filter(area__planta__id=id_planta, is_enabled=True).order_by("-updated")

    def post(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        fecha_inicial = self.request.POST.get("fInicial", None)
        fecha_final = self.request.POST.get("fFinal", None)

        if(queryset is not None):
            if fecha_final and fecha_final:
                queryset = queryset.filter(added >= fecha_inicial, added <= fecha_final)
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="Fugas.csv"'
            writer = csv.writer(response)
            writer.writerow(["area", "maquina", "ubicacion", "categoria", "recomendacion", "estatus", "nadp", "comentarios"])
            for fuga in queryset:
                writer.writerow(fuga.to_csv_row())
            return response
        else:
            return Http404

