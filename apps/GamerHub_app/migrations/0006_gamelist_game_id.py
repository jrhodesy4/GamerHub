# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-04 21:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GamerHub_app', '0005_auto_20171102_2135'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamelist',
            name='game_id',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]