# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-12 15:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='has_taken',
            field=models.NullBooleanField(default=None),
        ),
    ]