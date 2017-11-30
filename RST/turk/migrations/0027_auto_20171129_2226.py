# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-29 22:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turk', '0026_profile_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='position',
            field=models.CharField(choices=[('Temporary', 'Temporary'), ('Client', 'Client'), ('Developer', 'Developer')], default='Temporary', max_length=9),
        ),
    ]