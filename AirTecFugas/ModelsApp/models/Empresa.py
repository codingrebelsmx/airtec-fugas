# -*- coding: utf-8 -*-
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from .BaseModel import BaseModel


@python_2_unicode_compatible
class Empresa(BaseModel):
    """ Modelo que representa la entidad Empresa en la BD. """
    nombre = models.CharField("Nombre de la Empresa", max_length=100)
    descripcion = models.TextField(verbose_name="Descripción")

    def __str__(self):
        return self.nombre


    def __unicode__(self):
        return self.nombre