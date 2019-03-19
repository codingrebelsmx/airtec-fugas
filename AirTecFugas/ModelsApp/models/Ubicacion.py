# -*- coding: utf-8 -*-
from django.db import models
from .BaseModel import BaseModel
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Ubicacion(BaseModel):
    """ Model to represent abstract object called Ubicacion """
    nombre = models.CharField("Nombre", max_length=50)
    descripcion = models.CharField("Descripción", max_length=500, blank=True, null=True)

    # Custom Methods
    def __str__(self):
        return u"" + self.nombre


    def __unicode__(self):
        return u"" + self.nombre

