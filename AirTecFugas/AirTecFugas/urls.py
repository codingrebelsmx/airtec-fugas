"""
Definition of urls for AirTecFugas.
"""

from datetime import datetime
from django.conf.urls import url
from django.conf.urls import re_path
import django.contrib.auth.views
import MainApp
import WebApiApp

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = [# Examples:
    re_path(r'^', include('MainApp.urls')),
    re_path(r'^api/', include('WebApiApp.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    re_path(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    re_path(r'^admin/', admin.site.urls),]
