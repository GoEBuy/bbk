# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-18 07:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('content', models.TextField(verbose_name=b'content')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True, null=True)),
                ('published', models.BooleanField(default=True, verbose_name=b'notDraft')),
                ('poll_num', models.IntegerField(default=0)),
                ('comment_num', models.IntegerField(default=0)),
                ('keep_num', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'article',
                'verbose_name_plural': 'article',
            },
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('profile', models.CharField(default=b'', max_length=256, verbose_name=b'profile')),
                ('password', models.CharField(max_length=256, verbose_name=b'password')),
                ('register_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name=b'column_name')),
                ('intro', models.TextField(default=b'', verbose_name=b'introduction')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'column',
                'verbose_name_plural': 'column',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('poll_num', models.IntegerField(default=0)),
                ('article', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='focus.Article')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='focus.Article')),
                ('comment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='focus.Comment')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='focus.Author'),
        ),
        migrations.AddField(
            model_name='article',
            name='column',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='focus.Column', verbose_name=b'belong to'),
        ),
        migrations.AddField(
            model_name='article',
            name='user',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
