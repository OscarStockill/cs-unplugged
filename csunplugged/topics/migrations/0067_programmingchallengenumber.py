# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-12 08:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0066_lesson_programming_challenges_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProgrammingChallengeNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('challenge_set_number', models.PositiveSmallIntegerField()),
                ('challenge_number', models.PositiveSmallIntegerField()),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='topics.Lesson')),
                ('programming_challenge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='topics.ProgrammingChallenge')),
            ],
        ),
    ]
