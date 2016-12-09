# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-22 23:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_date', models.DateField(verbose_name='game date')),
                ('host', models.CharField(max_length=100)),
                ('guest', models.CharField(max_length=100)),
                ('host_score', models.IntegerField()),
                ('guest_score', models.IntegerField()),
            ],
        ),
    ]
