# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-14 11:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('content', tinymce.models.HTMLField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('published', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=9)),
                ('seo_title', models.CharField(blank=True, max_length=250, null=True)),
                ('seo_description', models.CharField(blank=True, max_length=250, null=True)),
                ('views', models.IntegerField(default=0)),
                ('tag', models.CharField(blank=True, max_length=30, null=True)),
                ('image', models.ImageField(upload_to='img')),
                ('featured', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('blurb', models.TextField(blank=True, default='', null=True)),
            ],
            options={
                'verbose_name': ('category',),
                'verbose_name_plural': 'categories',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.Blog')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='categories',
            field=models.ManyToManyField(to='blog.Category'),
        ),
        migrations.AddField(
            model_name='blog',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]