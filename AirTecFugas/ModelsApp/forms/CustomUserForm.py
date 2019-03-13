from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from ModelsApp.models import User
from ModelsApp.models import Empresa

class CustomUserCreationForm(UserCreationForm):

    #empresa =
    #forms.ModelChoiceField(queryset=Empresa.objects.filter(is_enabled=True),
    #required=False)
    empresa = forms.ModelChoiceField(queryset=Empresa.objects.filter(is_enabled=True))

    class Meta(UserCreationForm):
        model = User
        fields = ("username", "first_name", "last_name","empresa", "email")


class CustomUserChangeForm(UserChangeForm):

    #empresa =
    #forms.ModelChoiceField(queryset=Empresa.objects.filter(is_enabled=True),
    #required=False)
    empresa = forms.ModelChoiceField(queryset=Empresa.objects.filter(is_enabled=True))

    class Meta():
        model = User
        fields = '__all__'