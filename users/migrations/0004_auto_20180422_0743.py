# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-21 23:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20180421_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='session',
            field=models.CharField(blank=True, default='', help_text='\u7528\u6237\u767b\u5f55\u65f6\u4f1a\u5199\u5165\u5f53\u524dsession_key', max_length=50, null=True),
        ),
    ]