from django.views.generic import ListView
from ModelsApp.models import Fuga
from django.contrib.auth.mixins import PermissionRequiredMixin


class FugaListView(PermissionRequiredMixin, ListView):
    """ Abstract class to response for list of fugas request """
    model = Fuga
    template_name = "MainApp/Fuga/list-fuga.html"
    permission_required = ("ModelsApp.view_fuga",)
    

    def get_queryset(self):
        id_planta = self.request.session.get("id_planta", None)

        if id_planta == None:
            return super().get_object(queryset)
        else:
            return Fuga.objects.filter(area__planta__id=id_planta, is_enabled=True).order_by("-updated")



