# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-14 12:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity_platform', '0004_auto_20170314_2050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='post',
            name='published_date',
        ),
    ]
