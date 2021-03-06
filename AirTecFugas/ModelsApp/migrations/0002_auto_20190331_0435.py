# Generated by Django 2.1.7 on 2019-03-31 10:35

import ModelsApp.Helpers.UploadsTo
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ModelsApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagenfuga',
            name='imagen',
            field=models.ImageField(max_length=1000, upload_to=ModelsApp.Helpers.UploadsTo.get_full_path_img_fuga, verbose_name='Imagen de la fuga'),
        ),
        migrations.AlterField(
            model_name='planta',
            name='plano',
            field=models.FileField(max_length=500, upload_to=ModelsApp.Helpers.UploadsTo.get_full_path, verbose_name='Plano'),
        ),
    ]
