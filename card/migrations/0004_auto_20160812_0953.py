# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-12 09:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0003_auto_20160812_0839'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='book',
            new_name='books',
        ),
        migrations.RenameField(
            model_name='card',
            old_name='user',
            new_name='custom_users',
        ),
    ]
