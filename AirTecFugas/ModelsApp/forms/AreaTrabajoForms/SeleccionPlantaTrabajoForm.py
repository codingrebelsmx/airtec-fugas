# -*- coding: utf-8 -*-
from django import forms
from django.utils.encoding import python_2_unicode_compatible
from ModelsApp.models import Empresa

@python_2_unicode_compatible
class SeleccionPlantaTrabajoForm(forms.Form):
    """ Form to select Planta de Trabajo """
    cliente = forms.IntegerField(min_value=0)
    planta = forms.IntegerField(min_value=0)


    def __str__(self):
        return u"Seleccion Area de Trabajo"


    def __unicode__(self):
        return u"Seleccion Area de Trabajo"


