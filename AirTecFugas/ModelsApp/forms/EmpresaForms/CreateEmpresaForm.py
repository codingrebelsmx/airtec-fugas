# -*- coding: utf-8 -*-
from django import forms
from ModelsApp.models import Empresa


class CreateEmpresaForm(forms.ModelForm):
    """ Class to represents a form to create a new Empresa """

    class Meta:
        model = Empresa
        fields = ['nombre', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={"class":"form-control"}),
            'descripcion': forms.Textarea(attrs={"class":"form-control", "style":"resize:none;"}),
            }

