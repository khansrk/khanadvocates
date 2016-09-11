# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Court',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=400)),
                ('courttype', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('clientname', models.CharField(max_length=100)),
                ('mobile', models.IntegerField(max_length=50)),
                ('case_describe', models.TextField(max_length=2000)),
                ('status', models.CharField(max_length=1, choices=[(b'a', b'Approved'), (b's', b'Submitted'), (b'r', b'Rejected'), (b'p', b'Progress')])),
                ('hearing_date', models.DateTimeField(null=True, blank=True)),
                ('court', models.ForeignKey(to='advocates.Court')),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('casetype', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=1000)),
            ],
        ),
        migrations.AddField(
            model_name='session',
            name='track',
            field=models.ForeignKey(to='advocates.Track'),
        ),
    ]
