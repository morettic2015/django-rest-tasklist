# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-07 00:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasklist', '0003_auto_20190405_1444'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ('created',), 'verbose_name_plural': 'Tasks'},
        ),
    ]
