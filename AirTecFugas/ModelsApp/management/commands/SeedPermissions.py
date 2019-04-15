# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from django.contrib.auth.models import *
from django.utils.encoding import python_2_unicode_compatible
from django.core.exceptions import *
import sys

@python_2_unicode_compatible
class Command(BaseCommand):
    help = 'Seeds permisos de grupos y usuarios'
    admins = ["add_area",
                "change_area",
                "delete_area",
                "view_area",
                "add_empresa",
                "change_empresa",
                "delete_empresa",
                "view_empresa",
                "add_fuga",
                "change_fuga",
                "delete_fuga",
                "view_fuga",
                "add_imagenfuga",
                "change_imagenfuga",
                "delete_imagenfuga",
                "view_imagenfuga",
                "add_maquina",
                "change_maquina",
                "delete_maquina",
                "view_maquina",
                "add_planta",
                "change_planta",
                "delete_planta",
                "view_planta",
                "add_ubicacion",
                "change_ubicacion",
                "delete_ubicacion",
                "view_ubicacion",
                "add_user",
                "change_user",
                "delete_user",
                "view_user"]

    ejecutivos = ["add_area",
              "view_area",
                "view_empresa",
                "view_fuga",
                "view_imagenfuga",
                "view_maquina",
                "add_planta",
                "view_planta"]

    consultores = ["view_area",
                "view_empresa",
                "view_fuga",
                "view_imagenfuga",
                "view_maquina",
                "view_planta",
                "view_ubicacion"]

    tecnicos = ["add_area",
                "view_area",
                "view_empresa",
                "add_fuga",
                "delete_fuga",
                "view_fuga",
                "add_imagenfuga",
                "change_imagenfuga",
                "delete_imagenfuga",
                "view_imagenfuga",
                "add_maquina",
                "change_maquina",
                "view_maquina",
                "add_planta",
                "view_planta",
                "view_ubicacion"]

    grupos = {
        "Administradores": admins,
        "Ejecutivos":ejecutivos,
        "Consultores": consultores,
        "Tecnicos": tecnicos
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
                        permisoBD = all_permisos.filter(codename=permiso, content_type__app_label="ModelsApp").get()
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