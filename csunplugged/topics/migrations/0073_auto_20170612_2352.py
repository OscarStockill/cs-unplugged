# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-12 23:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0072_remove_lesson_age_range'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='age_range_temp',
        ),
        migrations.AddField(
            model_name='lesson',
            name='age_range',
            field=models.ManyToManyField(related_name='lessons', through='topics.LessonNumber', to='topics.AgeRange'),
        ),
    ]