# -*- coding: utf-8 -*-
from django import forms
from django.utils.encoding import python_2_unicode_compatible
from ModelsApp.models import Empresa

@python_2_unicode_compatible
class SeleccionPlantaTrabajoForm(forms.Form):
    """ Form to select Planta de Trabajo """
    cliente = forms.ModelChoiceField(queryset=Empresa.objects.filter(is_enabled=True), empty_label="Selecciona un cliente")
    planta = forms.ChoiceField()


    def __str__(self):
        return u"Seleccion Area de Trabajo"


    def __unicode__(self):
        return u"Seleccion Area de Trabajo"


