# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-24 06:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('turk', '0005_profile_role'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='role',
            new_name='isClient',
        ),
    ]