# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('preview_text', models.TextField(null=True, blank=True)),
                ('text', models.TextField(null=True, blank=True)),
                ('created', models.DateTimeField()),
                ('image', models.ImageField(null=True, upload_to=b'', blank=True)),
                ('publish', models.BooleanField(default=True)),
            ],
        ),
    ]
