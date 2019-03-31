# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from django.contrib.auth.models import *
from django.utils.encoding import python_2_unicode_compatible
from django.core.exceptions import *
import sys

@python_2_unicode_compatible
class Command(BaseCommand):
    help = 'Seeds permisos de grupos y usuarios'

    ciudadano = ["view_home",
                    "view_tramite",
                    "view_categoria",
                    "view_solicitud",
                    "view_solicitudes",
                    "view_home_documentos",
                    "view_ecdocumento",
                    "view_citas",
                    "view_formatos_llenos",
                    "update_formatos_llenos",
                    "download_formatos",
                    "download_ecdocumento",
                    "create_solicitud",
                    "create_cita",
                    "cancel_cita",
                    "edit_cita",
                    "change_user",
                    "change_ecciudadano",
                    "add_ecdireccion",
                    "change_ecdireccion",
                    "delete_ecdireccion",
                    "add_ecdocumento",
                    "change_ecdocumento",
                    "delete_ecdocumento",
                    "change_perfilapp",
                    "add_ectelefono",
                    "change_ectelefono",
                    "delete_ectelefono",
                    "change_notificacion",
                    "delete_notificacion",]

    grupos = {
        'Ciudadano': ciudadano
    }

    def __str__(self):
        return self.help

    def __unicode__(self):
        return self.help

    def _create_tags(self):
        all_permisos = Permission.objects.all()
        all_grupos = Group.objects.all()

        for (titulo, contenido) in self.grupos.items():
            
            try:
                grupoBD = all_grupos.filter(name=titulo).get()
                for permiso in contenido:
                    try:
                        permisoBD = all_permisos.filter(codename=permiso, content_type__app_label="EspacioCiudadano").get()
                        grupoBD.permissions.add(permisoBD)
                        print("==> Agregado '" + permisoBD.codename + "' a '" + grupoBD.name + "'")
                    except Permission.DoesNotExist:
                        print("*** No se encontro el permiso: '" + permiso + "' para el grupo ''" + titulo + "' en la BD.")
                    except MultipleObjectsReturned:
                        print("*** Se encontraron  multiples permisos con el nombre '" + permiso + "'.")
                grupoBD.save()
            except Group.DoesNotExist:
                print("*** No se encontro el grupo: '" + titulo + "' en la BD.")
            except MultipleObjectsReturned:
                print("*** Se encontraron  multiples grupos con el nombre '" + titulo + "'.")
            except:
                print("*** Ha ocurrido un error.")


    def handle(self, *args, **options):
        self._create_tags()