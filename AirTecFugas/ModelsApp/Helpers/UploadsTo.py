import uuid
import hashlib


""" Función que permite generar el path para los archivos que sube el ciudadano """
def get_full_path(instance, filename):
    return "{0}/{1}/{2}/{3}".format("PLANOS", instance.empresa.id, instance.nombre.upper(), filename)
