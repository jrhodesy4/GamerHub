# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-02 03:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GamerHub_app', '0003_auto_20171102_0326'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProPicture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, upload_to='documents/')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profilePic', to='GamerHub_app.User')),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='picture',
        ),
    ]
