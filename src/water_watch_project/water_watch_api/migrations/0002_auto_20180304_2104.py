# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-04 21:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('water_watch_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='station',
            old_name='latitutde',
            new_name='latitute',
        ),
        migrations.RenameField(
            model_name='station',
            old_name='longitutde',
            new_name='longitute',
        ),
    ]
