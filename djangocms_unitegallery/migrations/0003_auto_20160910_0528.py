# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-09 21:28
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_unitegallery', '0002_auto_20160910_0235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galleryphoto',
            name='image',
            field=filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.CASCADE, to='filer.Image'),
        ),
    ]