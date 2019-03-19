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

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = [# Examples:
    re_path(r'^$', default.home, name='home'),
    re_path(r'^contact$', default.contact, name='contact'),
    re_path(r'^about$', default.about, name='about'),
    re_path(r'^login/$',django.contrib.auth.views.LoginView.as_view(template_name= 'MainApp/login.html', 
                                                    authentication_form= BootstrapAuthenticationForm,
                                                    extra_context={ 'title': 'Log in', 'year': datetime.now().year,}),name = 'login'),
    re_path(r'^logout$',
        django.contrib.auth.views.LogoutView.as_view(),
        {
            'next_page': '/',
        },
        name = 'logout'),]
