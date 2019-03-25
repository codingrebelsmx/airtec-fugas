# -*- coding: utf-8 -*-
from django import forms
from ModelsApp.models import Planta, Empresa


class CreatePlantaForm(forms.ModelForm):
    """ Class to represents a form to create a new Planta """

    empresa = forms.ModelChoiceField(queryset=Empresa.objects.filter(is_enabled=True), 
                                    empty_label="Seleccione el cliente...", 
                                    widget=forms.Select(attrs={'class':'form-control'}))

    class Meta:
        model = Planta
        fields = ['nombre', 'descripcion', 'plano', 'empresa']
        widgets = {
            'nombre': forms.TextInput(attrs={"class":"form-control"}),
            'descripcion': forms.Textarea(attrs={"class":"form-control", "style":"resize:none;"}),
            }


