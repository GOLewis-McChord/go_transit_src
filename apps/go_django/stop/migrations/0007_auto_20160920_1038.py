# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-20 17:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stop', '0006_auto_20160920_0912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sign',
            name='anchor',
            field=models.CharField(choices=[('G', 'Sign is attached to a ground anchor.'), ('P', 'Sign is attached to a plate anchor.')], default='G', max_length=1),
        ),
        migrations.AlterField(
            model_name='sign',
            name='design',
            field=models.CharField(choices=[('A', '2015 Sign Design - Large Route Circles.'), ('B', '2016 Sign Design - Top Green Stripe, Modular Routes.')], default='B', max_length=1),
        ),
        migrations.AlterField(
            model_name='stop',
            name='available',
            field=models.IntegerField(choices=[(0, 'Stop was previously available and is no longer operating.'), (1, 'Stop is currently available.'), (2, 'Stop is not currently available but will be soon.'), (3, 'Stop has been scoped and there is a current effort to plan for it.'), (4, 'Stop has been identified but there is no current plan to implement it.')], default=2),
        ),
        migrations.AlterField(
            model_name='stop',
            name='description',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='stop',
            name='location_type',
            field=models.IntegerField(choices=[(0, 'Stop location where passengers board or disembark from a transit vehicle.'), (1, 'Station, physical structure, or area that contains more than one stop.')], default=0),
        ),
    ]
