# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-22 05:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0009_author_full_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='full_name',
        ),
    ]
