# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-27 22:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stop', '0005_auto_20160727_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stop',
            name='operating',
            field=models.DateField(blank=True, null=True),
        ),
    ]
