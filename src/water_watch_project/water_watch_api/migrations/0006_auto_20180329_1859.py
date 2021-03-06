# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-29 18:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('water_watch_api', '0005_auto_20180320_0157'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensortype',
            name='usgs_sensor_type_code',
            field=models.CharField(default='00000000', max_length=20),
        ),
        migrations.AlterField(
            model_name='sensortype',
            name='unit',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='station',
            name='latitude',
            field=models.DecimalField(decimal_places=12, max_digits=15),
        ),
        migrations.AlterField(
            model_name='station',
            name='longitude',
            field=models.DecimalField(decimal_places=12, max_digits=15),
        ),
    ]
