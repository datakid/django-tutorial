# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('texts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['last', 'first']},
        ),
        migrations.AlterModelOptions(
            name='translator',
            options={'ordering': ['last', 'first']},
        ),
        migrations.AddField(
            model_name='sourcetext',
            name='cover_colour',
            field=models.CharField(max_length=10, verbose_name=b'Colour', blank=True),
        ),
    ]
