# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-23 11:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity_platform', '0014_auto_20170323_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='詳細地點',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='post',
            name='詳細費用',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
