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
        fields = ['nombre', 'descripcion', 'flujo_total', 'horas_totales', 'plano', 'empresa']
        widgets = {
            'nombre': forms.TextInput(attrs={"class":"form-control"}),
            'descripcion': forms.Textarea(attrs={"class":"form-control", "style":"resize:none;"}),
            'plano': forms.FileInput(attrs={"accept":".svg"}),
            'flujo_total': forms.NumberInput(attrs={"step":"0.01", "min":"0"}),
            'horas_totales': forms.NumberInput(attrs={"step":"0.01", "min":"0"}),
            }


