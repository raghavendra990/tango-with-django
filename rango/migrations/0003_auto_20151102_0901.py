# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_auto_20151102_0753'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='like',
        ),
        migrations.RemoveField(
            model_name='category',
            name='views',
        ),
    ]
