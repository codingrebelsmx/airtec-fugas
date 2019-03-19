# -*- coding: utf-8 -*-
from django import forms
from ModelsApp.models import Fuga, Area, Ubicacion 

class CreateFugaForm(forms.ModelForm):
    """ Class to represents a form to create a new Fuga """

    area = forms.ModelChoiceField(queryset=Area.objects.filter(is_enabled=True), 
                                  empty_label="Seleccione una área...", 
                                  widget=forms.Select(attrs={'class': "form-control"}))

    ubicacion = forms.ModelChoiceField(queryset=Ubicacion.objects.filter(is_enabled=True), 
                                       empty_label="Seleccione una ubicación...", 
                                       widget=forms.Select(attrs={'class': "form-control"}))

    class Meta:
        model = Fuga
        fields = ['area', 'maquina', 'ubicacion', 'categoria', 'recomendacion', 'refacciones_comentarios', 'nadp']
        widgets = {
            'maquina': forms.Select(attrs={'class': "form-control"}),
            'categoria': forms.Select(attrs={'class': "form-control"}),
            'recomendacion': forms.Select(attrs={'class': "form-control"}),
            'refacciones_comentarios': forms.Textarea(attrs={'style':'resize:None;', 'class':'form-control'}),
            'nadp': forms.CheckboxInput(attrs={'class':"form-check-input"})
        }

