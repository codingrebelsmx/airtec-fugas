from django.views.generic import ListView
from ModelsApp.models import Fuga
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.mixins import PermissionRequiredMixin


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



