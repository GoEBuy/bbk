# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-14 05:23
from __future__ import unicode_literals

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('focus', '0007_auto_20180414_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='phone',
            field=models.CharField(blank=True, max_length=30, verbose_name='\u624b\u673a'),
        ),
        migrations.AlterField(
            model_name='newuser',
            name='username',
            field=models.CharField(default=b'', error_messages={b'unique': b'A user with that username already exists.'}, max_length=150, unique=True, validators=[django.contrib.auth.validators.ASCIIUsernameValidator()]),
        ),
    ]
