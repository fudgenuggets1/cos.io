# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-14 14:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0014_merge_20160914_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='bio',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]
