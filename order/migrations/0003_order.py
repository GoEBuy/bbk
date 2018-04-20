# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-18 03:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0002_logistics'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_state', models.IntegerField(choices=[(0, '\u672a\u4ed8\u6b3e'), (1, '\u5df2\u4ed8\u6b3e'), (2, '\u8fdb\u884c\u4e2d'), (3, '\u5df2\u5b8c\u6210'), (4, '\u9000\u8d27\u7533\u8bf7'), (5, '\u9000\u8d27\u4e2d'), (6, '\u5df2\u9000\u8d27'), (7, '\u53d6\u6d88\u4ea4\u6613'), (8, '\u5176\u4ed6'), (9, '\u672a\u77e5')], default=0, verbose_name='\u8ba2\u5355\u72b6\u6001')),
                ('order_price', models.CharField(default=0, max_length=30, verbose_name='\u8ba2\u5355\u4ef7\u683c')),
                ('pay_channel', models.IntegerField(choices=[(0, '\u73b0\u91d1'), (1, '\u5fae\u4fe1'), (2, '\u652f\u4ed8\u5b9d'), (3, '\u7b2c\u4e09\u65b9\u652f\u4ed8'), (4, '\u5176\u4ed6'), (5, '\u672a\u77e5')], default=0, verbose_name='\u652f\u4ed8\u6e20\u9053')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('pay_time', models.DateTimeField(auto_now=True)),
                ('deal_time', models.DateTimeField(auto_now=True, verbose_name='\u8ba2\u5355\u4ea4\u6613\u65f6\u95f4')),
                ('remark', models.CharField(max_length=250, verbose_name='\u7528\u6237\u5907\u6ce8')),
                ('address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='order.Address', verbose_name='\u6536\u8d27\u5730\u5740\u8868')),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('cate', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.Category', verbose_name='\u5206\u7c7b')),
                ('logistics_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='order.Logistics', verbose_name='\u7269\u6d41')),
            ],
            options={
                'verbose_name': '\u8ba2\u5355\u8868',
                'verbose_name_plural': '\u8ba2\u5355\u8868',
            },
        ),
    ]
