# -*- coding: utf-8 -*-
from django.db import models
from .BaseModel import BaseModel
from .Area import Area
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Maquina(BaseModel):
    """ Model to represent the abstract object called Maquina """
    nombre = models.CharField("Nombre", max_length=50)
    descripcion = models.CharField("Descripción", max_length=500, blank=True, null=True)
    area = models.ForeignKey(Area, on_delete=models.PROTECT, verbose_name="Área")

    # Custom Methods
    def __str__(self):
        return u"" + self.nombre


    def __unicode__(self):
        return u"" + self.nombre

