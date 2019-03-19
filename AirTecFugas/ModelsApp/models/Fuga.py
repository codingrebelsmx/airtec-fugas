# -*- coding: utf-8 -*-
from django.db import models
from .BaseModel import BaseModel
from .Area import Area
from .Maquina import Maquina
from .Ubicacion import Ubicacion
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Fuga(BaseModel):
    """ Model to represents the abstract object called Fuga """
    categorias = ((1,"Baja"),(2,"Normal"),(3, "Alta"))
    recomendaciones = (("REP", "Reparar"),("REM","Remplazar"),("OTR", "Otra"))
    estatus_fuga = ((1, "Registrado"),(2,"Corregido"))

    area = models.ForeignKey(Area, on_delete=models.PROTECT, verbose_name="Área")
    maquina = models.ForeignKey(Maquina, on_delete=models.PROTECT, verbose_name="Máquina")
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.PROTECT, verbose_name="Ubicación")
    categoria = models.SmallIntegerField("Categoría", choices=categorias)
    recomendacion = models.CharField("Recomendación", max_length=3, choices=recomendaciones) 
    refacciones_comentarios = models.CharField("Refacciones y/o comentarios", max_length=1000, blank=True, null=True)
    nadp = models.BooleanField("NADP", default=False)
    estatus = models.SmallIntegerField("Estatus", default=1, choices=estatus_fuga)

    #Custom Methods
    def __str__(self):
        return u"Fuga: " + str(self.id)


    def __unicode__(self):
        return u"Fuga: " + str(self.id)

