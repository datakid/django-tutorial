# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first', models.CharField(max_length=30, verbose_name='First Name')),
                ('other', models.CharField(max_length=30, verbose_name='Other Names', blank=True)),
                ('last', models.CharField(max_length=30, verbose_name='Last Name')),
                ('dob', models.DateField(null=True, verbose_name='Date of Birth', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SourceText',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('publisher', models.CharField(max_length=40, verbose_name='publisher')),
                ('date', models.DateField(null=True, blank=True)),
                ('place', models.CharField(max_length=20, verbose_name='place')),
                ('pages', models.CharField(max_length=5, verbose_name='pages', blank=True)),
                ('language', models.CharField(default='en', max_length=20, verbose_name='language', choices=[('it', 'Italian'), ('ja', 'Japanese'), ('es', 'Spanish'), ('zh-cn', 'Simplified Chinese'), ('zh-tw', 'Traditional Chinese'), ('en', 'English')])),
                ('authors', models.ManyToManyField(to='texts.Author', verbose_name='List of Authors')),
            ],
            options={
                'ordering': ['title'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TargetText',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('publisher', models.CharField(max_length=40, verbose_name='publisher')),
                ('date', models.DateField(null=True, blank=True)),
                ('place', models.CharField(max_length=20, verbose_name='place')),
                ('pages', models.CharField(max_length=5, verbose_name='pages', blank=True)),
                ('language', models.CharField(max_length=20, verbose_name='language', choices=[('it', 'Italian'), ('ja', 'Japanese'), ('es', 'Spanish'), ('zh-cn', 'Simplified Chinese'), ('zh-tw', 'Traditional Chinese'), ('en', 'English')])),
                ('source_text', models.ForeignKey(related_name='source', verbose_name='Source Text', to='texts.SourceText')),
            ],
            options={
                'ordering': ['title'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Translator',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first', models.CharField(max_length=30, verbose_name='First Name')),
                ('other', models.CharField(max_length=30, verbose_name='Other Names', blank=True)),
                ('last', models.CharField(max_length=30, verbose_name='Last Name')),
                ('dob', models.DateField(null=True, verbose_name='Date of Birth', blank=True)),
                ('original_name', models.CharField(max_length=40, verbose_name='Source Name', blank=True)),
                ('language', models.CharField(max_length=3, verbose_name='language', choices=[('it', 'Italian'), ('ja', 'Japanese'), ('es', 'Spanish'), ('zh-cn', 'Simplified Chinese'), ('zh-tw', 'Traditional Chinese'), ('en', 'English')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='targettext',
            name='translators',
            field=models.ManyToManyField(to='texts.Translator', verbose_name='List of Translators'),
            preserve_default=True,
        ),
    ]
