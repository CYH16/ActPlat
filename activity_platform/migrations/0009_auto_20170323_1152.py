# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-23 03:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity_platform', '0008_auto_20170318_0939'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='副標題',
            field=models.CharField(default='建議最多十四字', max_length=14),
        ),
        migrations.AlterField(
            model_name='post',
            name='活動名稱',
            field=models.CharField(default='建議最多十四字', max_length=14),
        ),
    ]