# -*- coding: utf-8 -*-
from django import forms
from ModelsApp.models import ImagenFuga


class CreateImgFugaForm(forms.ModelForm):
    """ Class to represents a form to create a new Image for a Fuga """


    class Meta:
        model = Area
        fields = ['nombre', 'descripcion', 'planta']
        widgets = {
            'nombre': forms.TextInput(attrs={"class":"form-control"}),
            'descripcion': forms.Textarea(attrs={"class":"form-control", "style":"resize:none;"}),
            }


