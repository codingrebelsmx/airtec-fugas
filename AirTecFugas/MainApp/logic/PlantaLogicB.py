from functools import reduce
from ModelsApp.models import Fuga, Planta


def get_planta(id_planta):
    planta = Planta.objects.filter(pk=id_planta).first()
    return planta


def get_dashboard_stats(id_planta, planta):
    cantidad_fugas = 0
    cantidad_fugas_resultas = 0
    ahorro_economico = 0.0
    ahorro_energetico = 0.0
    emisiones_co2 = 0.0

    if planta != None:
        fugas = Fuga.objects.filter(is_enabled=True, area__planta__pk=id_planta)
        fugas_pend = fugas.filter(estatus=1)
        fugas_resueltas = fugas.filter(estatus=2)

        cantidad_fugas = len(fugas)
        cantidad_fugas_resultas = len(fugas_resueltas)
        porcentaje_fugas = calcula_porcentaje_fugas(fugas_pend, planta)

        for f in fugas_resueltas:
            ahorro_economico+=f.ahorro_economico
            ahorro_energetico += f.ahorro_energetico

        emisiones_co2 = (ahorro_energetico * .42) / 1000

    return (cantidad_fugas, cantidad_fugas_resultas, porcentaje_fugas, ahorro_economico, ahorro_energetico, emisiones_co2)


def calcula_porcentaje_fugas(fugas, planta):
    porcentaje = 0
    if len(fugas) > 0 and float(planta.flujo_total) > 0:
        sumatoria = sum(x.flujo for x in fugas)
        porcentaje = sumatoria / float(planta.flujo_total)
    return porcentaje


#def calcula_ahorro_economico(fugas):
#    sumatoria = 0
#    if len(fugas) > 0:
#        sumatoria = sum(x.ahorro_economico for x in fugas)
#    return sumatoria


#def calcula_ahorro_energetico(fugas):
#    sumatoria = 0
#    if len(fugas) > 0:
#        sumatoria = sum(x.ahorro_energetico for x in fugas)
#    return sumatoria
def calcula_emisiones_co2(fugas):
    emisiones_co2 = 0
    ahorro_energetico = calcula_ahorro_energetico(fugas)
    emisiones_co2 = (ahorro_energetico * .42) / 1000
    return emisiones_co2

