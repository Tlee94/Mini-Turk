# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-01 08:55
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('turk', '0035_auto_20171201_0826'),
    ]

    operations = [
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='job',
            name='job_price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='job',
            name='bid_deadline',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 8, 8, 55, 4, 231984)),
        ),
        migrations.AddField(
            model_name='developer',
            name='job',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='turk.Job'),
        ),
    ]
