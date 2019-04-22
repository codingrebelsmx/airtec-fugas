from django import forms

class ExportCSVForm(forms.Form):
    """ Form for filter fugas to be exported to csv file """
    fecha_inicial = forms.DateField(label="Fecha Inicial", help_text="Fecha inicial para filtrar las fugas.")
    fecha_final = forms.DateField(label="Fecha Final", help_text="Fecha final para filtrar las fugas.")





