# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-21 18:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0004_auto_20160821_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='first_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='last_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
