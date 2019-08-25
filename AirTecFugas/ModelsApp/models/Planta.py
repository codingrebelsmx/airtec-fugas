# -*- coding: utf-8 -*-
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from .BaseModel import BaseModel
from .Empresa import Empresa
from ModelsApp.Helpers.UploadsTo import get_full_path
import os


@python_2_unicode_compatible
class Planta(BaseModel):
    """ Modelo que representa una planta de una empresa """

    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, verbose_name="Empresa")
    nombre = models.CharField("Nombre de la Planta", max_length=50)
    descripcion = models.CharField("Descripción", max_length=500, blank=True, null=True)
    plano = models.FileField(verbose_name = "Plano", upload_to=get_full_path, max_length=500)
    flujo_total = models.DecimalField(verbose_name="Flujo Total", null=True, decimal_places=2, max_digits=18)
    horas_totales = models.DecimalField(verbose_name = "Horas Totales Por Sucursal", null=True, decimal_places=2, max_digits=12)


    def get_extension(self):
        name , exten = os.path.splitext(self.plano.name)
        exten = exten.lower().replace(".","")
        return exten

    @property
    def porcentaje_fugas(self):
        fugas = fuga.objects.filter(area__planta__id=self.id)
        suma = 1

    @property
    def ahorro_economico(self):
        pass

    @property
    def emisiones_co2(self):
        pass

    @property
    def ahorro_energia(self):
        pass


    # Custom Methods
    def __str__(self):
        return self.nombre


    def __unicode__(self):
        return self.nombre

