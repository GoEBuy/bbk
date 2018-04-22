# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-20 23:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=20, verbose_name='\u6536\u8d27\u4eba\u8054\u7cfb\u7535\u8bdd')),
                ('phone_bak', models.CharField(max_length=20, verbose_name='\u5907\u7528\u8054\u7cfb\u7535\u8bdd')),
                ('country', models.CharField(default='', max_length=10)),
                ('province', models.CharField(default='', max_length=10)),
                ('city', models.CharField(default='', max_length=10)),
                ('area', models.CharField(default='', max_length=10)),
                ('street', models.CharField(default='', max_length=10)),
                ('zipcode', models.CharField(default='', max_length=10)),
                ('is_default_address', models.BooleanField(default=False)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '\u6536\u8d27\u5730\u5740\u8868',
                'verbose_name_plural': '\u6536\u8d27\u5730\u5740\u8868',
            },
        ),
        migrations.CreateModel(
            name='Logistics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyer_phone', models.CharField(max_length=20, verbose_name='\u6536\u8d27\u4eba\u8054\u7cfb\u7535\u8bdd')),
                ('buyer_phone_bak', models.CharField(max_length=20, verbose_name='\u5907\u7528\u8054\u7cfb\u7535\u8bdd')),
                ('seller_phone', models.CharField(max_length=20, verbose_name='\u6536\u8d27\u4eba\u8054\u7cfb\u7535\u8bdd')),
                ('seller_phone_bak', models.CharField(max_length=20, verbose_name='\u5907\u7528\u8054\u7cfb\u7535\u8bdd')),
                ('address', models.CharField(max_length=50, verbose_name='\u6536\u8d27\u5730\u5740')),
                ('zipcode', models.CharField(max_length=15, verbose_name='\u90ae\u653f\u7f16\u7801')),
                ('express_type', models.IntegerField(choices=[(0, 'ems'), (1, 'epress'), (2, 'other'), (3, 'none')], default=3, verbose_name='\u7269\u6d41\u65b9\u5f0f')),
                ('desc', models.CharField(max_length=150, verbose_name='\u63cf\u8ff0')),
            ],
            options={
                'verbose_name': '\u7269\u6d41\u8868',
                'verbose_name_plural': '\u7269\u6d41\u8868',
            },
        ),
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
            ],
            options={
                'verbose_name': '\u8ba2\u5355\u8868',
                'verbose_name_plural': '\u8ba2\u5355\u8868',
            },
        ),
        migrations.CreateModel(
            name='OrderRemark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_remark', models.IntegerField(default=0, verbose_name='\u8bc4\u8bba\u6570\u91cf')),
                ('content', models.CharField(max_length=300, verbose_name='\u8bc4\u4ef7\u5185\u5bb9')),
                ('score_service', models.IntegerField(default=3, verbose_name='\u670d\u52a1\u6001\u5ea6')),
                ('score_personal', models.IntegerField(default=3, verbose_name='\u4e13\u4e1a\u7a0b\u5ea6')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='\u8bc4\u4ef7\u65f6\u95f4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='\u8bc4\u4ef7\u65f6\u95f4')),
                ('state', models.IntegerField(default=1, verbose_name='\u662f\u5426\u5c55\u73b0')),
            ],
            options={
                'ordering': ['-id'],
                'verbose_name': '\u8ba2\u5355\u8bc4\u4ef7\u8868',
                'verbose_name_plural': '\u8ba2\u5355\u8bc4\u4ef7\u8868',
            },
        ),
    ]