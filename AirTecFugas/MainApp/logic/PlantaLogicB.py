from functools import reduce
from ModelsApp.models import Fuga, Planta


def get_planta(id_planta):
    planta = Planta.objects.filter(pk=id_planta).first()
    return planta

def get_cantidad_fugas(id_planta):
    fugas = Fuga.objects.filter(area__planta__pk=id_planta)
    cantidad_fugas = len(fugas)
    return cantidad_fugas


def get_cantidad_fugas_resueltas(id_planta):
    fugas = Fuga.objects.filter(area__planta__pk=id_planta, estatus=2)
    cantidad_fugas = len(fugas)
    return cantidad_fugas


def calcula_porcentaje_fugas(id_planta, planta):
    porcentaje = 0
    fugas = Fuga.objects.filter(area__planta__pk=id_planta, estatus=2)
    if len(fugas) > 0:
        sumatoria = sum(x.flujo for x in fugas)
        porcentaje = sumatoria / float(planta.flujo_total)
    return porcentaje


def calcula_ahorro_economico(id_planta):
    sumatoria = 0
    fugas = Fuga.objects.filter(area__planta__pk=id_planta, estatus=2)
    if len(fugas) > 0:
        sumatoria = sum(x.ahorro_economico for x in fugas)
    return sumatoria


def calcula_ahorro_energetico(id_planta):
    sumatoria = 0
    fugas = Fuga.objects.filter(area__planta__pk=id_planta, estatus=2)
    if len(fugas) > 0:
        sumatoria = sum(x.ahorro_energetico for x in fugas)
    return sumatoria


def calcula_emisiones_co2(id_planta):
    emisiones_co2 = 0
    ahorro_energetico = calcula_ahorro_energetico(id_planta)
    emisiones_co2 = (ahorro_energetico * .42) / 1000
    return emisiones_co2

