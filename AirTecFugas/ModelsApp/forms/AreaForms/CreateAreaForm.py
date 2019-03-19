# -*- coding: utf-8 -*-
from django import forms
from ModelsApp.models import Area, Planta

class CreateAreaForm(forms.ModelForm):
    """ Class to represents a form to create a new Area """

    planta = forms.ModelChoiceField(queryset=Planta.objects.filter(is_enabled=True), 
                                    empty_label="Seleccione la planta...", 
                                    widget=forms.Select(attrs={'class':'form-control'}))

    class Meta:
        model = Area
        fields = ['nombre', 'descripcion', 'planta']
        widgets = {
            'nombre': forms.TextInput(attrs={"class":"form-control"}),
            'descripcion': forms.Textarea(attrs={"class":"form-control", "style":"resize:none;"}),
            }

