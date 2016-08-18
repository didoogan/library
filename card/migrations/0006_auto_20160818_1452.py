# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-18 11:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0005_auto_20160818_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='myuser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='card', to='users.MyUser'),
        ),
    ]
