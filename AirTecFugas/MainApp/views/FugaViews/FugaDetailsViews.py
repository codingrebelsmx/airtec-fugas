# -*- coding: utf-8 -*-
from django.views.generic import DetailView
from django.http import HttpResponseRedirect, JsonResponse, HttpResponseNotFound, Http404
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect
from django.contrib.auth.mixins import PermissionRequiredMixin
from ModelsApp.models import Fuga, ImagenFuga
from ModelsApp.forms.FugaForms import CreateFugaForm


class FugaDetailView(PermissionRequiredMixin, DetailView):
    """ View to register a new Fuga """
    model = Fuga
    template_name = "MainApp/Fuga/detail-fuga.html"
    permission_required = ("ModelsApp.view_fuga",)



class ImagenesFugaDetailView(PermissionRequiredMixin, DetailView):
    model = Fuga
    template_name = ""
    permission_required = ("ModelsApp.view_fuga",)
    queryset = Fuga.objects.filter(is_enabled=True)


    def render_to_response(self, context, **response_kwargs):
        urls = []

        if self.object is not None:
            for img in self.object.imagenfuga_set.filter(is_enabled=True):
                urls.append({'url':reverse('imagen-fuga-view', args=[img.pk]) })
            return JsonResponse(urls, safe=False)
        else:
            raise Http404()


