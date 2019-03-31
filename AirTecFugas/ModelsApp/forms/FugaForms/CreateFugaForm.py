# -*- coding: utf-8 -*-
from django import forms
from ModelsApp.models import Fuga, Area, Ubicacion, Maquina, ImagenFuga 

class CreateFugaForm(forms.ModelForm):
    """ Class to represents a form to create a new Fuga """

    area = forms.ModelChoiceField(queryset=Area.objects.filter(is_enabled=True), 
                                  empty_label="Seleccione una área...",
                                  widget = forms.Select(attrs={'class':"form-control"}))

    ubicacion = forms.ModelChoiceField(queryset=Ubicacion.objects.filter(is_enabled=True), 
                                       empty_label="Seleccione una ubicación...",
                                       widget = forms.Select(attrs={'class':"form-control"}))

    imagen_1 = forms.ImageField(required=False, label="Imagen 1", help_text="Imagen 1 de la fuga")
    imagen_2 = forms.ImageField(required=False, label="Imagen 2", help_text="Imagen 2 de la fuga")

    def save(self, commit=True):
        instance = super().save(commit)
        #img_1 = self.cleaned_data["imagen_1"]
        #img_2 = self.cleaned_data["imagen_2"]

        #if img_1 != None:
        #   img = ImagenFuga(imagen=img_1, fuga=instance)
        #   img.save()
        #if img_2 != None:
        #    ImagenFuga(imagen=img_2, fuga=instance)
        #    img_2.save()
        return instance

    class Meta:
        model = Fuga
        fields = ['area', 'maquina', 'ubicacion', 'categoria', 'recomendacion', 'refacciones_comentarios', 'nadp', 'tecnico', 'punto_x', 'punto_y']
        widgets = {
            'maquina': forms.Select(attrs={'class': "form-control"}),
            'categoria': forms.Select(attrs={'class': "form-control"}),
            'recomendacion': forms.Select(attrs={'class': "form-control"}),
            'refacciones_comentarios': forms.Textarea(attrs={'style':'resize:None;', 'class':'form-control'}),
            'nadp': forms.CheckboxInput(attrs={'class':"form-check-input"}),
            'tecnico': forms.HiddenInput(),
            'punto_x':forms.HiddenInput(),
            'punto_y':forms.HiddenInput()
        }

