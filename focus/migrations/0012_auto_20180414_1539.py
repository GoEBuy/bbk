# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-14 07:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('focus', '0011_auto_20180414_1415'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newuser',
            old_name='sex',
            new_name='gender',
        ),
    ]
