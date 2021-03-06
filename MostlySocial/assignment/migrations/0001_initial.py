# Generated by Django 3.0.8 on 2021-05-21 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('follower_count', models.IntegerField()),
                ('following_count', models.IntegerField()),
                ('genre', models.CharField(max_length=200)),
                ('bio', models.CharField(max_length=300)),
                ('city', models.CharField(max_length=200)),
                ('contact_details', models.CharField(max_length=100)),
            ],
        ),
    ]
