# Generated by Django 3.0.8 on 2021-05-21 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='bio',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='account',
            name='city',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='account',
            name='contact_details',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='account',
            name='genre',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]