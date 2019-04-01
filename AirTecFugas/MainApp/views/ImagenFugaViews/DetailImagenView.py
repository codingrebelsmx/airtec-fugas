# -*- coding: utf-8 -*-
from django.views.generic import DetailView
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound, Http404
from django.contrib.auth.mixins import PermissionRequiredMixin
from ModelsApp.models import ImagenFuga
from ModelsApp.forms.FugaForms import CreateFugaForm


class DetailImagenView(PermissionRequiredMixin, DetailView):
    """ View to render an imagen as respone from request """
    model = ImagenFuga
    template_name = ""
    permission_required = ("ModelsApp.view_fuga",)
    queryset = ImagenFuga.objects.filter(is_enabled=True)


    def render_to_response(self, context, **response_kwargs):
        if self.object is not None and self.object.imagen is not None and self.object.imagen.name is not None and self.object.imagen.name != "":
            return HttpResponse(self.object.imagen.file, content_type=self.get_content_type(self.object.get_extension()))
        else:
            raise Http404()
    

    def get_content_type(self, extension):
        if extension == "jpg" or extension == "jpeg":
            return "image/jpg"
        elif extension == "png":
            return "image/png"
        elif extension == "gif":
            return "image/gif"
        elif extension == "ico":
            return "image/x-icon"
        elif extension == "svg":
            return "image/svg+xml"
        elif extension == "tiff" or extension == "tif":
            return "image/tiff"
        elif extension == "webp":
            return "image/webp"
        elif extension == "bmp":
            return "image/bmp"
