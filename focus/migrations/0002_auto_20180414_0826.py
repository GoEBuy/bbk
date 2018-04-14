# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-14 00:26
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('focus', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('cate_id', models.IntegerField(primary_key=True, serialize=False)),
                ('cate_name', models.CharField(max_length=20)),
                ('cate_desc', models.CharField(max_length=50, null=True, verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8')),
                ('state', models.IntegerField(default=0, verbose_name=b'\xe7\xb1\xbb\xe5\x88\xab\xe7\x8a\xb6\xe6\x80\x81')),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('pcate_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='focus.Category')),
            ],
        ),
        migrations.CreateModel(
            name='UserLoginInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login_time', models.DateTimeField(auto_now=True)),
                ('login_cnt', models.IntegerField(default=0, verbose_name=b'\xe7\x99\xbb\xe5\xbd\x95\xe6\xac\xa1\xe6\x95\xb0')),
            ],
        ),
        migrations.CreateModel(
            name='UserStar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('star_service', models.IntegerField(default=1, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x80\x81\xe5\xba\xa6')),
                ('star_personal', models.IntegerField(default=1, verbose_name=b'\xe4\xb8\x93\xe4\xb8\x9a\xe7\xa8\x8b\xe5\xba\xa6')),
                ('cate_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='focus.Category')),
            ],
        ),
        migrations.AddField(
            model_name='newuser',
            name='address',
            field=models.CharField(blank=True, max_length=20, verbose_name='\u5730\u5740'),
        ),
        migrations.AddField(
            model_name='newuser',
            name='city',
            field=models.CharField(blank=True, max_length=20, verbose_name='\u6240\u5728\u5730'),
        ),
        migrations.AddField(
            model_name='newuser',
            name='img',
            field=models.ImageField(blank=True, default=b'', upload_to=b'imgs/img_user'),
        ),
        migrations.AddField(
            model_name='newuser',
            name='phone',
            field=models.CharField(blank=True, max_length=20, verbose_name='\u624b\u673a'),
        ),
        migrations.AddField(
            model_name='newuser',
            name='sex',
            field=models.CharField(choices=[(b'F', b'Female'), (b'M', b'male'), (b'U', b'Unknown')], default=b'M', max_length=1),
        ),
        migrations.AlterField(
            model_name='newuser',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.ASCIIUsernameValidator()], verbose_name='username'),
        ),
        migrations.AddField(
            model_name='userstar',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userlogininfo',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
