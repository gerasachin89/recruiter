# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-10 15:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruiter', '0002_auto_20180710_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidatedetails',
            name='analytics_experience',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Analytics in Experience'),
        ),
    ]
