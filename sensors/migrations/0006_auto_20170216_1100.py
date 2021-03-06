# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-16 10:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sensors', '0005_remove_sensors_created_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sensors',
            options={'ordering': ['-sensor_types'], 'verbose_name': 'Sensor', 'verbose_name_plural': 'Sensors'},
        ),
        migrations.RenameField(
            model_name='sensors',
            old_name='text',
            new_name='description',
        ),
    ]
