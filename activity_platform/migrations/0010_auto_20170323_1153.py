# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-23 03:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity_platform', '0009_auto_20170323_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='副標題',
            field=models.CharField(default='建議最多十四字', max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='活動名稱',
            field=models.CharField(default='建議最多十四字', max_length=30),
        ),
    ]