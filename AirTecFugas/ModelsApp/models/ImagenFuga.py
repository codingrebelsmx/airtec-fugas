# -*- coding: utf-8 -*-
from django.db import models
from .BaseModel import BaseModel
from .Fuga import Fuga
from ModelsApp.Helpers.UploadsTo import get_full_path
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class ImagenFuga(BaseModel):
    """ Model to represents the abstract object called ImagenFuga """
    imagen = models.ImageField("Imagen de la fuga", upload_to=get_full_path)
    fuga = models.ForeignKey(Fuga, on_delete=models.PROTECT)


