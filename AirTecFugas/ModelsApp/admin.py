from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from ModelsApp.models.Empresa import Empresa
from ModelsApp.models.Planta import Planta
from ModelsApp.models.User import User

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Empresa)
admin.site.register(Planta)

