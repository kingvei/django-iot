# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-26 19:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interactions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twittervote',
            name='log',
            field=models.TextField(default=b'', editable=False),
        ),
    ]