# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-14 21:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stop', '0004_sign_midi_guide'),
    ]

    operations = [
        migrations.AddField(
            model_name='shelter',
            name='ad_panel',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='shelter',
            name='solar_lighting',
            field=models.BooleanField(default=False),
        ),
    ]
