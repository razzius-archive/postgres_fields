# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.postgres.fields.hstore

from django.contrib.postgres.operations import HStoreExtension


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        HStoreExtension(),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=254)),
                ('email', models.EmailField(max_length=254)),
                ('preferences', django.contrib.postgres.fields.hstore.HStoreField()),
            ],
        ),
    ]
