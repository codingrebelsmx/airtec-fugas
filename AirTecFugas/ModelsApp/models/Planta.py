# -*- coding: utf-8 -*-
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from .BaseModel import BaseModel
from .Empresa import Empresa
from ModelsApp.Helpers.UploadsTo import get_full_path


@python_2_unicode_compatible
class Planta(BaseModel):
    """ Modelo que representa una planta de una empresa """

    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, verbose_name="Empresa")
    nombre = models.CharField("Nombre de la Planta", max_length=50)
    descripcion = models.CharField("Descripción", max_length=500, blank=True, null=True)
    plano = models.FileField(verbose_name = "Plano", upload_to=get_full_path)

    # Custom Methods
    def __str__(self):
        return self.nombre


    def __unicode__(self):
        return self.nombre

