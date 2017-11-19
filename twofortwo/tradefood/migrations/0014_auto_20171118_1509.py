# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-18 15:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tradefood', '0013_auto_20171118_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='retail_value',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='retail_value',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]