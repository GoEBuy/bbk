# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-24 13:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20180524_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='img',
            field=models.ImageField(blank=True, default='default-avatar.png', upload_to='imgs/img_user', verbose_name='\u5934\u50cf'),
        ),
    ]
