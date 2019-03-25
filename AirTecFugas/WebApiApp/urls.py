"""
Definition of urls for WebApi App.
"""

from django.conf.urls import re_path
from WebApiApp.views import MaquinaViews, AreaViews, UbicacionViews, CategoriaViews
from WebApiApp.views import EstatusFugaViews, RecomendacionFugaViews, PlantaViews, EmpresaViews


urlpatterns = [### -------------- LIST API PARA SELECTS -------------- ###
    re_path(r'^empresa/list-select/$', EmpresaViews.EmpresaListSelectView.as_view({'get': 'list'}), name='ApiEmpresaListSelect'),
    re_path(r'^planta/list-select/(?P<id_empresa>[0-9]+)/$', PlantaViews.PlantaListSelectView.as_view({'get': 'list'}), name='ApiPlantaListSelect'),
    re_path(r'^area/list-select/$', AreaViews.AreaListSelectView.as_view({'get': 'list'}), name='ApiAreaListSelect'),
    re_path(r'^maquina/list-select/(?P<id_area>[0-9]+)/$', MaquinaViews.MaquinaListSelectView.as_view({'get': 'list'}), name='ApiMaquinaListSelect'),
    re_path(r'^ubicacion/list-select/$', UbicacionViews.UbicacionListSelectView.as_view({'get': 'list'}), name='ApiUbicacionListSelect'),
    re_path(r'^categoria-fuga/list-select/$', CategoriaViews.CategoriaListSelectView.as_view({'get': 'list'}), name='ApiCategoriaListSelect'),
    re_path(r'^recomendacion-fuga/list-select/$', RecomendacionFugaViews.RecomendacionFugaListSelectView.as_view({'get': 'list'}), name='ApiRecomendacionFugaListSelect'),]

