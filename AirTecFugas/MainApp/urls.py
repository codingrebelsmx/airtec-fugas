"""
Definition of urls for AirTecFugas.
"""

from datetime import datetime
from django.conf.urls import url
from django.conf.urls import re_path
import django.contrib.auth.views
from django.conf import settings
from django.conf.urls.static import static

from MainApp.forms import BootstrapAuthenticationForm
from MainApp.views import default
from MainApp.views.FugaViews import FugaCreateView, FugaListView, FugaDetailsViews, FugaEditView, FugaDeleteView, FugaExportCSVFormView
from MainApp.views.AreaViews import AreaCreateView, AreaCreatePartialView, AreaListView, AreaEditsView, AreaDeleteView
from MainApp.views.MaquinaViews import MaquinaCreateView, MaquinaCreatePartialView, MaquinaListView, MaquinaEditViews, MaquinaDeleteView
from MainApp.views.PlantaViews import SeleccionPlantaTrabajoView, CreatePlantaPartialView, PlanoPlantaView, PlanoPlantaImgView
from MainApp.views.EmpresaViews import CreateEmpresaPartialView
from MainApp.views.ImagenFugaViews import DetailImagenView
from MainApp.views.Mapa.MapaOpenLayerViews import MapaFugasOpenLayerView

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = [# Examples:
    re_path(r'^$', default.home, name='home'),
    re_path(r'^dashboard/$', default.dashboard, name='dashboard'),
    re_path(r'^contact$', default.contact, name='contact'),
    re_path(r'^about$', default.about, name='about'),

    ### -------------- CRUD EMPRESA -------------- ###
    re_path(r'^empresa/create/$', CreateEmpresaPartialView.as_view(), name='empresa-create'),
    #re_path(r'^empresa/edit/(?P<pk>\d+)/$', default.about,
    #name='empresa-edit'),
    #re_path(r'^empresa/details/(?P<pk>\d+)/$', default.about,
    #name='empresa-details'),
    re_path(r'^empresa/list/$', default.about, name='empresa-list'),

    ### -------------- CRUD PLANTA -------------- ###
    re_path(r'^planta/seleccionar-planta/$', SeleccionPlantaTrabajoView.as_view(), name='selec-planta-trabajo'),
    re_path(r'^planta/plano/(?P<pk>\d+)/$', PlanoPlantaView.as_view(), name='planta-plano-view'),
    re_path(r'^planta/plano_img/(?P<pk>\d+)/$', PlanoPlantaImgView.as_view(), name='planta-plano-view'),
    re_path(r'^planta/create/$', CreatePlantaPartialView.as_view(), name='planta-create'),
    re_path(r'^planta/list/$', default.about, name='planta-list'),

    ### -------------- CRUD FUGA -------------- ###
    re_path(r'^mapa-fugas/$', default.mapafugas, name='mapa-fugas'),

    re_path(r'^mapafugas/$', MapaFugasOpenLayerView.as_view(), name='mapa-fugas-ol'),

    re_path(r'^fuga/create/(?P<punto_x>-?\d+\.\d+)/(?P<punto_y>-?\d+\.\d+)/$', FugaCreateView.as_view(), name='fuga-create'),
    re_path(r'^fuga/edit/(?P<pk>\d+)/$', FugaEditView.FugaEditView.as_view(), name='fuga-edit'),
    #re_path(r'^fuga/edit/mapa/(?P<pk>\d+)/$', FugaEditView, name='fuga-edit'),
    re_path(r'^fuga/delete/(?P<pk>\d+)/$', FugaDeleteView.as_view(), name='fuga-delete'),
    re_path(r'^fuga/partial-edit/(?P<pk>\d+)/$', FugaEditView.FugaPartialEditView.as_view(), name='fuga-partial-edit'),
    re_path(r'^fuga/corregida/(?P<pk>\d+)/$', FugaEditView.FugaCorregidaEditView.as_view(), name='fuga-corregida'),
    re_path(r'^fuga/details/(?P<pk>\d+)/$', FugaDetailsViews.FugaDetailView.as_view(), name='fuga-details'),
    re_path(r'^fuga/partial-details/(?P<pk>\d+)/$', FugaDetailsViews.FugaDetailPartialView.as_view(), name='fuga-partial-details'),
    re_path(r'^fuga/imagenes/(?P<pk>\d+)/$', FugaDetailsViews.ImagenesFugaDetailView.as_view(), name='fuga-images'),
    re_path(r'^fuga/list/$', FugaListView.as_view(), name='fuga-list'),
    re_path(r'^fuga/export/csv/$', FugaExportCSVFormView.as_view(), name='fuga-export-csv'),

    ### -------------- CRUD AREA -------------- ###
    re_path(r'^area/create/$', AreaCreateView.as_view(), name='area-create'),
    re_path(r'^area/partial-create/$', AreaCreatePartialView.as_view(), name='area-create-partial'),

    re_path(r'^area/partial-edit/(?P<pk>\d+)/$', AreaEditsView.AreaPartialEditView.as_view(), name='area-partial-edit'),
    re_path(r'^area/partial-delete/(?P<pk>\d+)/$', AreaDeleteView.as_view(), name='area-delete'),
    re_path(r'^area/list/$', AreaListView.as_view(), name='area-list'),

    ### -------------- CRUD MAQUINA -------------- ###
    re_path(r'^maquina/create/$', MaquinaCreateView.as_view(), name='maquina-create'),
    re_path(r'^maquina/partial-create/$', MaquinaCreatePartialView.as_view(), name='maquina-create-partial'),

    re_path(r'^maquina/partial-edit/(?P<pk>\d+)/$', MaquinaEditViews.MaquinaPartialEditView.as_view(), name='maquina-partial-edit'),
    re_path(r'^maquina/partial-delete/(?P<pk>\d+)/$', MaquinaDeleteView.as_view(), name='maquina-partial-delete'),
    re_path(r'^maquina/list/$', MaquinaListView.as_view(), name='maquina-list'),

    ### -------------- IMAGENES FUGA -------------- ###
    re_path(r'^imagen-fuga/detail/(?P<pk>\d+)/$', DetailImagenView.as_view(), name='imagen-fuga-view'),

    re_path(r'^login/$',django.contrib.auth.views.LoginView.as_view(template_name= 'MainApp/Authentication/login.html', 
                                                    authentication_form= BootstrapAuthenticationForm,
                                                    redirect_authenticated_user=True,
                                                    extra_context={ 'title': 'Log in', 'year': datetime.now().year,}),name = 'login'),
    re_path(r'^logout$', django.contrib.auth.views.LogoutView.as_view(),name = 'logout')]
