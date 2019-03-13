# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _
from ModelsApp.models.Empresa import Empresa
from ModelsApp.models.Planta import Planta
from ModelsApp.models.User import User
from ModelsApp.forms.CustomUserForm import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User

    list_display = ['email', 'username', 'empresa']
    fieldsets = (('Información General', {'fields': ('username', 'password', 'empresa')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),)
    add_fieldsets = (('Información General', {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'empresa', 'is_staff'),
        }),)


# Register your models here.
admin.site.register(Empresa)
admin.site.register(Planta)
admin.site.register(User, CustomUserAdmin)

