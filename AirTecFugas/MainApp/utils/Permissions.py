# -*- coding: utf-8 -*-
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.views import redirect_to_login
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.http import HttpResponseForbidden, Http404
from django.contrib.auth.models import User
from EspacioCiudadano.models import Ciudadano
from EspacioCiudadano.utils.SearcherInstance import SearcherInstance
from IttenEC_BA import settings


class LoggedInPermissionsMixin(PermissionRequiredMixin):

    def dispatch(self, request, *args, **kwargs):
        authenticated = self.request.user.is_authenticated

        if not authenticated:
            return redirect_to_login(self.request.get_full_path(),
                                     self.get_login_url(), self.get_redirect_field_name())

        if not self.has_permission():
            raise PermissionDenied(self.get_permission_denied_message())

        return super().dispatch(request, *args, **kwargs)
