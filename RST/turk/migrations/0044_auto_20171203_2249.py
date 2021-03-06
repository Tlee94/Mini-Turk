# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-03 22:49
from __future__ import unicode_literals

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turk', '0043_auto_20171203_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='bid_deadline',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 10, 22, 49, 28, 982196)),
        ),
        migrations.AlterField(
            model_name='job',
            name='lowest_bid',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
