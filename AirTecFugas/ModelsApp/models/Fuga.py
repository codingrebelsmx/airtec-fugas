# -*- coding: utf-8 -*-
from django.db import models
from .BaseModel import BaseModel
from .Area import Area
from .Maquina import Maquina
from .Ubicacion import Ubicacion
from .User import User
# from .ImagenFuga import ImagenFuga
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Fuga(BaseModel):
    """ Model to represents the abstract object called Fuga """

    # Categorias
    categorias = ((1,"1"),(2,"2"),(3, "3"))
    categorias_dict = [{"id":1, "nombre": "1"},{"id":2, "nombre": "2"},{"id":3, "nombre": "3"}]
    # Recomendaciones de la fuga
    recomendaciones = (("REP", "Reparar"),("REM","Remplazar"),("OTR", "Otra"))
    recomendaciones_dict = [{"id":"REP", "nombre":"Reparar"},{"id":"REM", "nombre":"Remplazar"},{"id":"OTR", "nombre": "Otra"}]
    # Estatus de la fuga
    estatus_fuga = ((1, "Registrado"),(2,"Corregido"))
    estatus_fuga_dict = [{"id":1, "nombre":"Registrado"},{"id":2,"nombre":"Corregido"}]

    area = models.ForeignKey(Area, on_delete=models.PROTECT, verbose_name="Área")
    maquina = models.ForeignKey(Maquina, on_delete=models.PROTECT, verbose_name="Máquina")
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.PROTECT, verbose_name="Ubicación")
    categoria = models.SmallIntegerField("Categoría", choices=categorias)
    recomendacion = models.CharField("Recomendación", max_length=3, choices=recomendaciones) 
    refacciones_comentarios = models.CharField("Refacciones y/o comentarios", max_length=1000, blank=True, null=True)
    nadp = models.BooleanField("Not Available During Production (NADP)", default=False)
    estatus = models.SmallIntegerField("Estatus", default=1, choices=estatus_fuga)
    tecnico = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Técnico Registró")
    punto_x = models.DecimalField(verbose_name="Coordenada X", max_digits=26, decimal_places=18)
    punto_y = models.DecimalField(verbose_name="Coordenada Y", max_digits=26, decimal_places=18)

    @property
    def imagenes(self):
        return self.imagenfuga_set.filter(is_enabled=True)
        #return ImagenFuga.objects.filter(fuga__id=self.pk, is_enabled=True)

    def to_csv_row(self):
        return [self.area.nombre, self.maquina.nombre, self.ubicacion.nombre, self.categoria
                , self.recomendacion_csv, self.estatus_csv, self.nadp_csv, self.refacciones_comentarios
                , self.flujo, self.ahorro_economico, self.ahorro_energetico]

    @property
    def recomendacion_csv(self):
        if self.recomendacion == "REP":
            return "Reparar"
        elif self.recomendacion == "REM":
            return "Remplazar"
        elif self.recomendacion == "OTR":
            return "Otra"

    @property
    def estatus_csv(self):
        if self.estatus == 1:
            return "Registrado"
        elif self.estatus == 2:
            return "Corregido"

    @property
    def nadp_csv(self):
        return "Si" if self.nadp else "No"

    @property
    def flujo(self):
        return (float(self.categoria) * 1.2)

    @property
    def ahorro_economico(self):
        horas_totales = float(self.area.planta.horas_totales)
        return (((self.flujo * 60 * horas_totales) / 1000) * 0.42)

    @property
    def ahorro_energetico(self):
        horas_totales = float(self.area.planta.horas_totales)
        return ((self.flujo / 4) * 0.7459 * horas_totales)

    #Custom Methods
    def __str__(self):
        return u"Fuga: " + str(self.id)


    def __unicode__(self):
        return u"Fuga: " + str(self.id)

