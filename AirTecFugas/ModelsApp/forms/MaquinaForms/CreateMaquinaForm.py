# -*- coding: utf-8 -*-
from django import forms
from ModelsApp.models import Maquina, Area


class CreateMaquinaForm(forms.ModelForm):
    """ Class to represents a form to create a new record of Maquina """

    area = forms.ModelChoiceField(queryset=Area.objects.filter(is_enabled=True))


    class Meta:
        model = Maquina
        fields = ['nombre', 'descripcion', 'area']

