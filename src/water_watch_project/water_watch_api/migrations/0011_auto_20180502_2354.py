# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-02 16:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('water_watch_api', '0010_station_station_short_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sensordata',
            options={'ordering': ['id', 'sensor_data_dateTime', 'sensor__station_id', 'sensor__sensor_type_id'], 'verbose_name_plural': 'sensor data'},
        ),
        migrations.AlterField(
            model_name='station',
            name='station_short_name',
            field=models.CharField(default='Short Name', max_length=255, null=True),
        ),
    ]