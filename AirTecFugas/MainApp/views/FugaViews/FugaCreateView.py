# -*- coding: utf-8 -*-
from django.views.generic import CreateView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.mixins import PermissionRequiredMixin
from ModelsApp.models import Fuga, ImagenFuga
from ModelsApp.forms.FugaForms import CreateFugaForm


class FugaCreateView(PermissionRequiredMixin, CreateView):
    """ View to register a new Fuga """
    model = Fuga
    form_class = CreateFugaForm
    template_name = "MainApp/Fuga/create-fuga.html"
    success_url = reverse_lazy('fuga-list')
    permission_required = ("ModelsApp.add_fuga",)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        punto_x = self.kwargs.get('punto_x',None)
        punto_y = self.kwargs.get('punto_y',None)
        id_tecnico = self.request.user.id
        context["id_tecnico"] = id_tecnico
        context["punto_x"] = punto_x
        context["punto_y"] = punto_y
        return context

    def dispatch(self, request, *args, **kwargs):
        cliente = self.request.session.get("id_cliente", None)
        planta = self.request.session.get("id_planta", None)

        if cliente != None and planta != None:
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect('selec-planta-trabajo')


    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.tecnico = self.request.user.id
        return obj


    def form_valid(self, form):
        result = super().form_valid(form)
        if type(result) is HttpResponseRedirect:

            img1 = form.files.get("imagen_1",None)
            if img1 != None:
                imgFuga = ImagenFuga()
                imgFuga.fuga = self.object
                imgFuga.imagen = img1
                imgFuga.imagen.save(img1.name,img1)
                
            img2 = form.files.get("imagen_2",None)
            if img2 != None:
                imgFuga = ImagenFuga()
                imgFuga.fuga = self.object
                imgFuga.imagen = img2
                imgFuga.imagen.save(img2.name,img2)

        return result

