# Generated by Django 5.1.6 on 2025-03-05 08:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Star',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('birth_date', models.DateField()),
                ('content', models.TextField()),
                ('is_published', models.BooleanField(default=True)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('categories', models.ManyToManyField(related_name='stars', to='star.category')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stars', to='star.country')),
            ],
            options={
                'verbose_name': 'Знаменитость',
                'verbose_name_plural': 'Знаменитости',
                'ordering': ['name'],
            },
        ),
    ]
