# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-12 13:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otherUser', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Favorites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otherUser', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('gender', models.CharField(blank=True, max_length=20)),
                ('lookingFor', models.CharField(blank=True, max_length=20)),
                ('radius', models.IntegerField(blank=True)),
                ('isNotification', models.BooleanField(default=False)),
                ('isBeacon', models.BooleanField(default=False)),
                ('subscriptionDate', models.CharField(blank=True, max_length=50)),
                ('biography', models.CharField(blank=True, max_length=10000)),
                ('profilePictureURL', models.CharField(blank=True, max_length=200)),
                ('deviceToken', models.CharField(blank=True, max_length=150)),
                ('facebookToken', models.CharField(blank=True, max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name='favorites',
            name='userID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='friendsZones.User'),
        ),
        migrations.AddField(
            model_name='block',
            name='userID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='friendsZones.User'),
        ),
    ]
