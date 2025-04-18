# Generated by Django 5.1.6 on 2025-03-05 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('star', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='star',
            options={},
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, verbose_name='URL'),
        ),
        migrations.AddField(
            model_name='country',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, verbose_name='URL'),
        ),
    ]
