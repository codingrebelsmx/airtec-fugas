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
from MainApp.views.FugaViews import FugaCreateView
from MainApp.views.AreaViews import AreaCreateView, AreaCreatePartialView
from MainApp.views.MaquinaViews import MaquinaCreateView, MaquinaCreatePartialView
from MainApp.views.PlantaViews import SeleccionPlantaTrabajoView, CreatePlantaPartialView, PlanoPlantaView
from MainApp.views.EmpresaViews import CreateEmpresaPartialView


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
    re_path(r'^planta/create/$', CreatePlantaPartialView.as_view(), name='planta-create'),
    #re_path(r'^planta/edit/(?P<pk>\d+)/$', default.about, name='planta-edit'),
    #re_path(r'^planta/details/(?P<pk>\d+)/$', default.about,
    #name='planta-details'),
    re_path(r'^planta/list/$', default.about, name='planta-list'),

    ### -------------- CRUD FUGA -------------- ###
    re_path(r'^fuga/create/$', FugaCreateView.as_view(), name='fuga-create'),
    re_path(r'^fuga/edit/(?P<pk>\d+)/$', default.about, name='fuga-edit'),
    re_path(r'^fuga/details/(?P<pk>\d+)/$', default.about, name='fuga-details'),
    re_path(r'^fuga/list/$', default.about, name='fuga-list'),

    ### -------------- CRUD AREA -------------- ###
    re_path(r'^area/create/$', AreaCreateView.as_view(), name='area-create'),
    re_path(r'^area/create/partial/$', AreaCreatePartialView.as_view(), name='area-create-partial'),
    re_path(r'^area/edit/(?P<pk>\d+)/$', default.about, name='area-edit'),
    re_path(r'^area/details/(?P<pk>\d+)/$', default.about, name='area-details'),
    re_path(r'^area/list/$', default.about, name='area-list'),

    ### -------------- CRUD MAQUINA -------------- ###
    re_path(r'^maquina/create/$', MaquinaCreateView.as_view(), name='maquina-create'),
    re_path(r'^maquina/create/partial/$', MaquinaCreatePartialView.as_view(), name='maquina-create-partial'),
    re_path(r'^maquina/edit/(?P<pk>\d+)/$', default.about, name='maquina-edit'),
    re_path(r'^maquina/details/(?P<pk>\d+)/$', default.about, name='maquina-details'),
    re_path(r'^maquina/list/$', default.about, name='maquina-list'),

    re_path(r'^login/$',django.contrib.auth.views.LoginView.as_view(template_name= 'MainApp/Authentication/login.html', 
                                                    authentication_form= BootstrapAuthenticationForm,
                                                    redirect_authenticated_user=True,
                                                    extra_context={ 'title': 'Log in', 'year': datetime.now().year,}),name = 'login'),
    re_path(r'^logout$', django.contrib.auth.views.LogoutView.as_view(),name = 'logout'),
    re_path(r'^mapa-fugas/$', default.mapafugas, name='mapa-fugas')]
