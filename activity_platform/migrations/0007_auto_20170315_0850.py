# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-15 00:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity_platform', '0006_post_圖片'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='圖片',
            field=models.TextField(default='.jpg'),
        ),
    ]