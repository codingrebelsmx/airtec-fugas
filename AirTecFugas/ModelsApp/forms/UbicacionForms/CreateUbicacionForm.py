# -*- coding: utf-8 -*-
from django import forms
from ModelsApp.models import Ubicacion

class CreateUbicacionForm(forms.ModelForm):
    """ Class to represents a form to create a new record of Ubicacion """

    class Meta:
        model = Ubicacion
        fields = ['nombre', 'descripcion']
