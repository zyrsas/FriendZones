# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-17 10:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friendsZones', '0004_auto_20180112_1316'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='latitude',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='user',
            name='longitude',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]