# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advocates', '0003_delete_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='court',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='session',
            name='track',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.DeleteModel(
            name='Court',
        ),
        migrations.DeleteModel(
            name='Track',
        ),
    ]
