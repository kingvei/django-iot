# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-26 22:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('observations', '0002_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='color',
            name='device',
        ),
        migrations.DeleteModel(
            name='Color',
        ),
    ]
