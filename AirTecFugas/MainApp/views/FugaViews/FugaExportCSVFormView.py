# -*- coding: utf-8 -*-
from django.views.generic import FormView
from django.http import HttpResponse, Http404
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.mixins import PermissionRequiredMixin
from ModelsApp.models import Fuga
from ModelsApp.forms.FugaForms import ExportCSVForm
import csv


class FugaExportCSVFormView(PermissionRequiredMixin, FormView):
    """ View to export fugas to csv file """
    model = Fuga
    form_class = ExportCSVForm
    template_name = "MainApp/Fuga/export-csv-fuga.html"
    permission_required = ("ModelsApp.view_fuga",)
    success_url = reverse_lazy("fuga-list")


    def get_queryset(self, fecha_inicial, fecha_final):
        id_planta = self.request.session.get("id_planta", None)

        if id_planta == None:
            return super().get_queryset(queryset)
        else:
            if fecha_final and fecha_final:
                return Fuga.objects.filter(area__planta__id=id_planta, is_enabled=True, added__date__gte= fecha_inicial, added__date__lte = fecha_final).order_by("-updated")
            else:
                return Fuga.objects.filter(area__planta__id=id_planta, is_enabled=True).order_by("-updated")


    def post(self, request, *args, **kwargs):
        fecha_inicial = self.request.POST.get("fInicial", None)
        fecha_final = self.request.POST.get("fFinal", None)

        queryset = self.get_queryset(fecha_inicial, fecha_final)

        if(queryset is not None):
            #if fecha_final and fecha_final:
            #    queryset = queryset.filter(added >= fecha_inicial, added <=
            #    fecha_final)
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="Fugas.csv"'
            writer = csv.writer(response)
            writer.writerow(["Área", "Máquina", "Ubicación", "Categoría", "Recomendación", "Estatus", "NADP", "Comentarios"])
            for fuga in queryset:
                writer.writerow(fuga.to_csv_row())
            return response
        else:
            return Http404





