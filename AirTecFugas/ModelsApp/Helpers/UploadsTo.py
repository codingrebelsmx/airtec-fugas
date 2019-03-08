import uuid
import hashlib


""" Función que permite generar el path para los archivos que sube el ciudadano """
def get_full_path(instance, filename):
    carpeta = hashlib.sha1(str(instance.ciudadano.pk).encode("ascii","ignore")).hexdigest()
    sub_carpeta = hashlib.sha1(str(instance.tipo_documento).encode("ascii","ignore")).hexdigest()
    str_file_name = hashlib.sha1(str(instance.subtipo_documento).encode("ascii","ignore")).hexdigest() + "." + instance.get_extension()
    return "{0}/{1}/{2}".format(carpeta, sub_carpeta, str_file_name)
