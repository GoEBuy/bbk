# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-18 04:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_auto_20180418_1221'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='logistics_id',
            new_name='logistics',
        ),
    ]
