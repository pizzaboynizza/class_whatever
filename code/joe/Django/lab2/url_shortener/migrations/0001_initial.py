# Generated by Django 3.0.5 on 2020-04-03 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UrlShortener',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_code', models.CharField(max_length=7, unique=True)),
                ('long_link', models.CharField(max_length=200, unique=True)),
            ],
        ),
    ]