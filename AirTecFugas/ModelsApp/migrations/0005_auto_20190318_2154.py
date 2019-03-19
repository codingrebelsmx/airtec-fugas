# Generated by Django 2.1.7 on 2019-03-19 03:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ModelsApp', '0004_auto_20190313_1721'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_enabled', models.BooleanField(default=True, verbose_name='Habilitado')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('descripcion', models.CharField(blank=True, max_length=255, null=True, verbose_name='Descripción')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Fuga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_enabled', models.BooleanField(default=True, verbose_name='Habilitado')),
                ('categoria', models.SmallIntegerField(choices=[(1, 'Baja'), (2, 'Normal'), (3, 'Alta')], verbose_name='Categoría')),
                ('recomendacion', models.CharField(choices=[('REP', 'Reparar'), ('REM', 'Remplazar'), ('OTR', 'Otra')], max_length=3, verbose_name='Recomendación')),
                ('refacciones_comentarios', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Refacciones y/o comentarios')),
                ('nadp', models.BooleanField(default=False, verbose_name='NADP')),
                ('estatus', models.SmallIntegerField(choices=[(1, 'Registrado'), (2, 'Corregido')], default=1, verbose_name='Estatus')),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ModelsApp.Area', verbose_name='Área')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Maquina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_enabled', models.BooleanField(default=True, verbose_name='Habilitado')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('descripcion', models.CharField(blank=True, max_length=500, null=True, verbose_name='Descripción')),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ModelsApp.Area', verbose_name='Área')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Ubicacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_enabled', models.BooleanField(default=True, verbose_name='Habilitado')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('descripcion', models.CharField(blank=True, max_length=500, null=True, verbose_name='Descripción')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='empresa',
            name='descripcion',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='planta',
            name='descripcion',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Descripción'),
        ),
        migrations.AddField(
            model_name='fuga',
            name='maquina',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ModelsApp.Maquina', verbose_name='Máquina'),
        ),
        migrations.AddField(
            model_name='fuga',
            name='ubicacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ModelsApp.Ubicacion', verbose_name='Ubicación'),
        ),
        migrations.AddField(
            model_name='area',
            name='planta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ModelsApp.Planta', verbose_name='Planta'),
        ),
    ]