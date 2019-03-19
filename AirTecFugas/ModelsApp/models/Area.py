# -*- coding: utf-8 -*-
from django.db import models
from .BaseModel import BaseModel
from .Planta import Planta
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Area(BaseModel):
    """ Model to represent the abstract object called Area """
    nombre = models.CharField("Nombre", max_length=50)
    descripcion = models.CharField("Descripción", max_length=255, blank=True, null=True)
    planta = models.ForeignKey(Planta, on_delete=models.PROTECT, verbose_name="Planta")

    # Custom Methods
    def __str__(self):
        return u"" + self.nombre


    def __unicode__(self):
        return u"" + self.nombre

