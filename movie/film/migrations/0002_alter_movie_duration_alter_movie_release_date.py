# Generated by Django 5.0.1 on 2024-02-12 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='duration',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.CharField(max_length=20),
        ),
    ]
