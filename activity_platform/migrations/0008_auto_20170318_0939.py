# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-18 01:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity_platform', '0007_auto_20170315_0850'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='標籤',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='post',
            name='類型',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]