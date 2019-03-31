# -*- coding: utf-8 -*-
import uuid
import hashlib


""" Función que permite generar el path para los archivos svg de cada planta """
def get_full_path(instance, filename):
    planos_nombre_folder = hashlib.sha1("PLANOS".encode("ascii","ignore")).hexdigest()
    empresa_nombre_folder = hashlib.sha1(str(instance.empresa.pk).encode("ascii","ignore")).hexdigest()
    plano_nombre_archivo = str(instance.empresa.pk) + "-" + str(instance.pk)
    plano_nombre_archivo = hashlib.sha1(plano_nombre_archivo.encode("ascii","ignore")).hexdigest() + "." + instance.get_extension()
    return "{0}/{1}/{2}".format(planos_nombre_folder, empresa_nombre_folder, plano_nombre_archivo)


""" Función que permite generar el path para los archivos que suben por cada fuga """
def get_full_path_img_fuga(instance, filename):
    imgs_fugas_nombre_folder = hashlib.sha1("FUGAS_IMG".encode("ascii","ignore")).hexdigest()
    planta_nombre_folder = hashlib.sha1(str(instance.fuga.area.planta.pk).encode("ascii","ignore")).hexdigest()
    area_nombre_folder = hashlib.sha1(str(instance.fuga.area.pk).encode("ascii","ignore")).hexdigest()
    fuga_nombre_folder = hashlib.sha1(str(instance.fuga.pk).encode("ascii","ignore")).hexdigest()
    img_nombre_archivo = str(instance.fuga.area.pk) + "-" + str(instance.fuga.pk) + "-" + str(instance.added)
    img_nombre_archivo = hashlib.sha1(img_nombre_archivo.encode("ascii","ignore")).hexdigest() + "." + instance.get_extension()
    return "{0}/{1}/{2}/{3}/{4}".format(imgs_fugas_nombre_folder, planta_nombre_folder, area_nombre_folder, fuga_nombre_folder, img_nombre_archivo)

