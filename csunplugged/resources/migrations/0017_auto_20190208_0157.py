# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-08 01:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0016_auto_20181105_0901'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='content_mi',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='resource',
            name='name_mi',
            field=models.CharField(default='', max_length=200, null=True),
        ),
    ]