# Generated by Django 5.1.2 on 2024-10-08 21:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Inmuebles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servicios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montoAgua', models.FloatField()),
                ('montoLuz', models.FloatField()),
                ('montoGas', models.FloatField()),
                ('pagadoAgua', models.BooleanField(default=False)),
                ('pagadoLuz', models.BooleanField(default=False)),
                ('pagadoGas', models.BooleanField(default=False)),
                ('propiedad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inmuebles.propiedades')),
            ],
        ),
    ]
