# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-09 18:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_timerange', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timerange',
            name='cmsplugin_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='djangocms_timerange_timerange', serialize=False, to='cms.CMSPlugin'),
        ),
    ]
