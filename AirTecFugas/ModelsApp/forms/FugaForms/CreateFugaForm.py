# -*- coding: utf-8 -*-
from django import forms
from ModelsApp.models import Fuga, Area, Ubicacion 

class CreateFugaForm(forms.ModelForm):
    """ Class to represents a form to create a new Fuga """

    area = forms.ModelChoiceField(queryset=Area.objects.filter(is_enabled=True))
    ubicacion = forms.ModelChoiceField(queryset=Ubicacion.objects.filter(is_enabled=True))

    class Meta:
        model = Fuga
        fields = ['area', 'maquina', 'ubicacion', 'categoria', 'recomendacion', 'refacciones_comentarios', 'nadp']
        widgets = {
            'area': forms.Select(attrs={'class': "form-control"}),
            'maquina': forms.Select(attrs={'class': "form-control"}),
            'ubicacion': forms.Select(attrs={'class': "form-control"}),
            'categoria': forms.Select(attrs={'class': "form-control"}),
            'recomendacion': forms.Select(attrs={'class': "form-control"}),
            'refacciones_comentarios': forms.Textarea(attrs={'cols': 25, 'rows': 20, 'style':'resize:None;'}),
            'nadp': forms.CheckboxInput(attrs={'class':"custom-control-input"})
        }

