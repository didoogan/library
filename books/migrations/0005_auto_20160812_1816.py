# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-12 15:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20160812_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='has_taken',
            field=models.BooleanField(default=False),
        ),
    ]