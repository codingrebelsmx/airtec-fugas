# Generated by Django 2.1.7 on 2019-08-24 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ModelsApp', '0004_planta_flujo_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='planta',
            name='horas_totales',
            field=models.DecimalField(decimal_places=2, max_digits=12, null=True, verbose_name='Horas Totales Por Sucursal'),
        ),
    ]
