# -*- coding: utf-8 -*-
from django.db import models
from .BaseModel import BaseModel
from .Fuga import Fuga
from ModelsApp.Helpers.UploadsTo import get_full_path_img_fuga
from django.utils.encoding import python_2_unicode_compatible
import os

@python_2_unicode_compatible
class ImagenFuga(BaseModel):
    """ Model to represents the abstract object called ImagenFuga """

    imagen = models.ImageField("Imagen de la fuga", upload_to=get_full_path_img_fuga, max_length=1000)
    fuga = models.ForeignKey(Fuga, on_delete=models.PROTECT)


    def get_extension(self):
        name , exten = os.path.splitext(self.imagen.name)
        exten = exten.lower().replace(".","")
        return exten


    def get_content_type(self):
        name , exten = os.path.splitext(self.imagen.name)
        exten = exten.lower().replace(".","")
        return exten


    def __str__(self):
        return self.imagen.name


    def __unicode__(self):
        return u"" + self.imagen.name

