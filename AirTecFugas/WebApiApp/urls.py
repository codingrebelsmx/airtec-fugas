"""
Definition of urls for WebApi App.
"""

from django.conf.urls import re_path
from WebApiApp.views import MaquinaViews


urlpatterns = [re_path(r'^maquina/list-select/(?P<id_area>[0-9]+)/$', MaquinaViews.MaquinaListSelectView.as_view({'get': 'list'}), name='ApiMaquinaListSelect'),]
