# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-20 17:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('route', '0003_auto_20160920_0912'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stopseq',
            name='load_seq',
        ),
        migrations.AlterField(
            model_name='joint',
            name='headway',
            field=models.IntegerField(default=1200),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='end',
            field=models.TimeField(default='18:00:00'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='offset',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='start',
            field=models.TimeField(default='07:00:00'),
        ),
        migrations.AlterField(
            model_name='segmentorder',
            name='dir_type',
            field=models.CharField(choices=[('I', 'Inbound (return) trip'), ('L', 'Loop (one-direction) trip that returns to trip origin'), ('O', 'Outbound (originating) trip')], default='O', max_length=1),
        ),
        migrations.AlterField(
            model_name='segmentorder',
            name='order',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='stopseq',
            name='timed',
            field=models.IntegerField(choices=[(0, 'Times are considered approximate.'), (1, 'Times are considered exact.')], default=0),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='transfer_type',
            field=models.IntegerField(choices=[(0, 'Transfer is only recommended but no timing is involved.'), (1, 'Transfer is timed to ensure tranfer between stops.')], default=1),
        ),
    ]
