# -*- coding: utf-8 -*-
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class BaseModel(models.Model):
    """ Modelo base de los modelos """

    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_enabled = models.BooleanField(default=True, verbose_name='Habilitado')
    
    # Custom Methods
    def __str__(self):
        return self.added
    
    
    def __unicode__(self):
        return self.added


    class Meta:
        abstract = True

