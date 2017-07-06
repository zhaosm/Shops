# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-06 05:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20170706_0042'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request_Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to_user', models.CharField(blank=True, default='无ID', max_length=32, verbose_name='好友ID')),
            ],
            options={
                'verbose_name': '给我申请的好友',
                'verbose_name_plural': '给我申请的好友',
                'db_table': 'Request_Friend',
            },
        ),
        migrations.RemoveField(
            model_name='user',
            name='request_friend',
        ),
        migrations.AddField(
            model_name='request_friend',
            name='from_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]